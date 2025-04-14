import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import os
import asyncio
import time
import logging

# Path ke ffmpeg
FFMPEG_PATH = "D:/RYAN/BOT/ffmpeg-7.1.1-essentials_build/bin/ffmpeg.exe"

# Logging di console
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s"
)

# Aktifkan intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Cooldown per channel agar suara tidak spam
last_trigger_time = {}
cooldown = 2  # detik

@bot.event
async def on_ready():
    logging.info(f'✅ Bot aktif sebagai {bot.user.name}')

async def play_audio(vc):
    if not vc.is_connected():
        logging.warning("❗ Gagal memutar audio karena VC tidak terkoneksi.")
        return

    if os.path.exists("masuk.mp3") and not vc.is_playing():
        vc.play(FFmpegPCMAudio("masuk.mp3", executable=FFMPEG_PATH))
        while vc.is_playing():
            await asyncio.sleep(0.5)

@bot.event
async def on_voice_state_update(member, before, after):
    if member.bot:
        return

    now = time.time()
    voice_client = discord.utils.get(bot.voice_clients, guild=member.guild)

    # USER MASUK VC
    if not before.channel and after.channel:
        if now - last_trigger_time.get(after.channel.id, 0) < cooldown:
            return
        last_trigger_time[after.channel.id] = now

        logging.info(f"🎧 {member.display_name} masuk ke VC: {after.channel.name}")

        if not voice_client or not voice_client.is_connected():
            try:
                voice_client = await after.channel.connect()
                logging.info("✅ Bot berhasil join VC.")
            except discord.ClientException as e:
                logging.error(f"❌ Bot sudah join di VC lain: {e}")
                return
            except Exception as e:
                logging.error(f"❌ Gagal join VC: {e}")
                return

        if voice_client.channel == after.channel:
            await play_audio(voice_client)

    # USER KELUAR DARI VC
    if before.channel and before.channel != after.channel:
        vc_channel = before.channel
        members = [m for m in vc_channel.members if not m.bot]
        if len(members) == 0:
            if voice_client and voice_client.channel == vc_channel:
                await voice_client.disconnect()
                logging.info("👋 Bot keluar karena channel kosong.")

# Fitur auto-restart jika bot error/crash
if __name__ == "__main__":
    while True:
        try:
            bot.run("ISI TOKEN KAMU")  # Ganti dengan token asli
        except Exception as e:
            logging.error(f"❌ Bot crash: {e}")
            logging.info("🔁 Restart bot dalam 5 detik...")
            time.sleep(5)
