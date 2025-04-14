# 🎙️ Discord Voice Channel Greeter Bot

![Python](https://img.shields.io/badge/Python-3.6+-blue?logo=python&logoColor=white)
![Discord.py](https://img.shields.io/badge/discord.py-API-green?logo=discord)
![License](https://img.shields.io/badge/License-MIT-blue.svg)
![FFmpeg](https://img.shields.io/badge/FFmpeg-required-critical?logo=ffmpeg)
![PM2](https://img.shields.io/badge/PM2-optional-lightgrey?logo=pm2)

> Bot Python yang secara otomatis **menyapa pengguna dengan audio** ketika mereka masuk ke voice channel di Discord!

---

## ✨ Fitur

- 🔊 Menyapa anggota yang bergabung ke voice channel dengan audio otomatis.
- 🛡️ Mencegah spam sapaan dengan sistem cooldown.
- 👋 Otomatis keluar dari voice channel jika channel kosong.
- 🧾 Logging aktivitas bot secara real-time ke konsol.

---

## 📦 Prasyarat

Pastikan Anda sudah menginstal:

- ✅ Python **3.6 atau lebih baru**
- ✅ **FFmpeg** (tersedia di [ffmpeg.org](https://ffmpeg.org/download.html))
- ✅ **Token bot Discord** aktif
- 🔄 **PM2** *(opsional, untuk manajemen proses)*

---

## ⚙️ Instalasi

### 1. Clone Repository
```bash
git clone https://github.com/11neuty/bot-dc.git
cd <NAMA_FOLDER>
```
### 2. Instalasi Dependensi
```bash
pip install discord.py
```
### 3. Download FFmpeg
Unduh dari situs resmi FFmpeg.

Ekstrak dan catat path ke ffmpeg.exe (untuk Windows) atau binary-nya (untuk Mac/Linux).

### 4. Konfigurasi Bot
Ganti ISI TOKEN KAMU di dalam skrip Python dengan token bot Discord Anda.

Sesuaikan FFMPEG_PATH ke lokasi executable FFmpeg yang sudah Anda unduh.

## 🚀 Menjalankan Bot
### 📌 Tanpa PM2:
```bash
python bot.py
```
### 📌 Dengan PM2 (opsional):
```bash
pm2 start bot.py --name "discord-greeter-bot"
```
### 🎧 Penggunaan
Setelah bot aktif, ia akan otomatis menyapa pengguna yang bergabung ke voice channel dengan memutar file masuk.mp3.

Pastikan file masuk.mp3 berada di direktori yang sama dengan file bot.py.

### 🧠 Logging
Bot menggunakan modul logging untuk mencatat aktivitas secara real-time. Semua aktivitas bisa Anda pantau langsung dari terminal.

