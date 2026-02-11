# YukBicara - Speech Recognition & Analysis App 🎙️

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

Aplikasi latihan berbicara bahasa Indonesia dengan fitur analisis akurasi, kecepatan berbicara, dan perbandingan hasil menggunakan teknologi Speech Recognition berbasis AI.


## 📋 Deskripsi

**YukBicara** adalah aplikasi desktop berbasis Python yang dirancang untuk membantu pengguna melatih dan meningkatkan kemampuan berbicara bahasa Indonesia. Aplikasi ini menggunakan teknologi Speech Recognition untuk menganalisis pengucapan dan memberikan feedback real-time.

### 🎯 Tujuan Aplikasi
- Melatih kemampuan artikulasi dan pengucapan
- Meningkatkan kecepatan berbicara yang optimal
- Memberikan feedback objektif terhadap akurasi pengucapan
- Membantu persiapan presentasi, pidato, atau public speaking

---

## ✨ Fitur Utama

### 🎤 Fitur Utama
- **Input Teks Referensi**: Masukkan teks yang ingin dilatih atau dibacakan
- **Pilihan Kecepatan**: Tiga kategori kecepatan berbicara
  - 🐢 Slow (110 WPM)
  - 🚶 Average (140 WPM)
  - 🏃 Fast (170 WPM)
- **Rekam Audio**: Rekam suara melalui mikrofon dengan kualitas tinggi
- **Analisis Real-time**: 
  - ✅ Persentase akurasi pengucapan
  - ⚡ Kecepatan berbicara (Words Per Minute)
  - ❌ Deteksi kata yang salah diucapkan

### 🆕 Fitur Tambahan
- **Display Hasil Rekaman**: Tampilan teks hasil konversi speech-to-text
- **Halaman Perbandingan**: Window khusus untuk membandingkan:
  - Teks referensi vs Teks hasil rekaman (side-by-side)
  - Jumlah kata pada kedua teks
  - Daftar detail kata yang salah
- **Playback Audio**: Putar ulang rekaman untuk evaluasi mandiri
- **Estimasi Waktu**: Perkiraan waktu berbicara berdasarkan jumlah kata dan kecepatan

---

## 🛠️ Teknologi yang Digunakan

| Teknologi | Fungsi |
|-----------|--------|
| **Python 3.x** | Bahasa pemrograman utama |
| **Tkinter** | GUI framework untuk interface desktop |
| **SpeechRecognition** | Konversi suara ke teks (Google Speech API) |
| **NLTK** | Natural Language Toolkit untuk analisis teks dan edit distance |
| **Pygame** | Audio playback dan multimedia handling |
| **Pyphen** | Syllable counting untuk perhitungan kecepatan berbicara |

---

## 📦 Instalasi

### Persyaratan Sistem
- Python 3.7 atau lebih baru
- Mikrofon aktif
- Koneksi internet (untuk Google Speech Recognition API)
- Sistem operasi: Windows / Linux / MacOS

### Langkah Instalasi

#### 1️⃣ Clone Repository
```bash
git clone https://github.com/intunn7/Speech-Recognition.git
cd Speech-Recognition
```

#### 2️⃣ Install Dependencies
```bash
pip install SpeechRecognition nltk pygame pyphen
```

Atau gunakan file requirements.txt:
```bash
pip install -r requirements.txt
```

#### 3️⃣ Persiapan File
Pastikan file **`BG-01.png`** (background image) tersedia di direktori yang sama dengan script `YUKBICARAA.py`.

#### 4️⃣ Jalankan Aplikasi
```bash
python YUKBICARAA.py
```

---

## 🚀 Cara Menggunakan

### Langkah-langkah Penggunaan:

1. **📝 Input Teks**
   - Masukkan teks yang ingin Anda latih pada kolom "Masukkan teks Anda"
   - Contoh: "Selamat pagi, hari ini saya akan mempresentasikan tentang teknologi AI"

2. **⚙️ Pilih Kecepatan**
   - Pilih kategori kecepatan berbicara yang sesuai:
     - **Slow (110 WPM)**: Untuk pemula atau latihan artikulasi
     - **Average (140 WPM)**: Kecepatan normal berbicara
     - **Fast (170 WPM)**: Untuk presentasi atau pidato cepat

3. **✅ Konfirmasi**
   - Klik tombol **"Enter"** untuk melihat:
     - Jumlah kata dalam teks
     - Estimasi waktu berbicara

4. **🎙️ Mulai Rekam**
   - Klik tombol **"Rekam"**
   - Tunggu hingga mikrofon aktif
   - Bacakan teks referensi dengan jelas
   - Aplikasi akan otomatis mendeteksi selesai

5. **📊 Lihat Hasil**
   - **Akurasi**: Persentase keakuratan pengucapan (0-100%)
   - **Kecepatan Berbicara**: WPM (Words Per Minute) aktual
   - **Kata yang Salah**: Daftar kesalahan pengucapan
   - **Hasil Rekaman**: Teks yang berhasil dikenali sistem

6. **🔍 Analisis Detail**
   - Klik **"Lihat Hasil"** untuk membuka window perbandingan
   - Bandingkan teks referensi dengan hasil rekaman
   - Lihat jumlah kata dan detail kesalahan

7. **🔊 Playback**
   - Klik **"Playback"** untuk mendengar ulang rekaman Anda
   - Evaluasi pengucapan secara mandiri

---

## 📸 Screenshot

### Tampilan Utama
```
┌─────────────────────────────────────────────────────────┐
│  YukBicara - Speech Recognition                         │
├─────────────────────────────────────────────────────────┤
│  [Teks Referensi Display]                               │
│                                                          │
│  Masukkan teks Anda: [________________]                 │
│  Kecepatan: [Average (140 WPM) ▼]                       │
│  [Enter]  [Rekam]  [Playback]                           │
│                                                          │
│  Akurasi: 95.5%                                         │
│  Kecepatan: 142 WPM                                     │
│  [Kata yang Salah Display]                              │
│  [Hasil Rekaman Display]  [Lihat Hasil]                 │
└─────────────────────────────────────────────────────────┘
```

### Window Perbandingan
```
┌─────────────────────────────────────────────────────────┐
│  Hasil Perbandingan                                     │
├─────────────────────────────────────────────────────────┤
│  Teks Referensi:                    Jumlah Kata: 25    │
│  [Teks lengkap...]                                      │
│                                                          │
│  Teks Hasil Rekaman:                Jumlah Kata: 24    │
│  [Teks lengkap...]                                      │
│                                                          │
│  Kata-kata yang Salah:                                  │
│  - Seharusnya "teknologi", Anda ucapkan "tekonologi"   │
└─────────────────────────────────────────────────────────┘
```

---

## 🎯 Use Cases

### 1. 🎓 Pendidikan
- Latihan membaca teks bahasa Indonesia
- Pembelajaran diksi dan artikulasi
- Persiapan ujian lisan

### 2. 💼 Profesional
- Persiapan presentasi bisnis
- Latihan public speaking
- Training communication skills

### 3. 🎭 Presentasi & Pidato
- Melatih kecepatan berbicara ideal
- Memastikan pengucapan yang jelas
- Mengukur durasi pidato

### 4. 🏥 Terapi Wicara
- Monitoring progress terapi
- Latihan pengucapan kata sulit
- Evaluasi objektif kemajuan

---

## 🔧 Troubleshooting

### ❌ Error: "gangguan jaringan"
**Penyebab:**
- Google Speech API tidak terhubung
- Mikrofon tidak menangkap suara dengan jelas
- Koneksi internet terputus

**Solusi:**
- ✅ Pastikan koneksi internet stabil
- ✅ Periksa apakah mikrofon berfungsi (tes di aplikasi lain)
- ✅ Berbicara lebih jelas dengan volume yang cukup
- ✅ Kurangi noise di lingkungan sekitar

### ❌ Error: "BG-01.png not found"
**Solusi:**
- ✅ Pastikan file `BG-01.png` ada di folder yang sama dengan `YUKBICARAA.py`
- ✅ Atau modifikasi baris 28 di kode: `self.bg = PhotoImage(file="BG-01.png")`

### ❌ Mikrofon tidak terdeteksi
**Solusi:**
- ✅ Periksa izin akses mikrofon di sistem operasi
- ✅ Windows: Settings → Privacy → Microphone → Allow apps
- ✅ MacOS: System Preferences → Security & Privacy → Microphone
- ✅ Pastikan mikrofon terhubung dengan benar

### ❌ Akurasi selalu rendah
**Tips:**
- 🎤 Gunakan mikrofon berkualitas baik
- 🔇 Rekam di ruangan yang tenang
- 🗣️ Berbicara dengan jelas dan tidak terburu-buru
- 📏 Jaga jarak yang konsisten dengan mikrofon (10-15 cm)

### ❌ Error saat instalasi dependencies
**Solusi:**
```bash
# Upgrade pip terlebih dahulu
python -m pip install --upgrade pip

# Install satu per satu jika error
pip install SpeechRecognition
pip install nltk
pip install pygame
pip install pyphen
```

---

## 📊 Algoritma & Metodologi

### Perhitungan Akurasi
Menggunakan **Levenshtein Distance (Edit Distance)** dari NLTK:
```
Akurasi = (1 - EditDistance/MaxLength) × 100%
```

### Perhitungan Kecepatan
```
WPM = (Jumlah Suku Kata / Durasi Audio dalam detik) × 60
```

### Deteksi Kesalahan
Membandingkan word-by-word antara teks referensi dan hasil recognition:
- Mengabaikan tanda baca
- Case-insensitive comparison
- Mencatat setiap perbedaan kata

---

## 📝 Catatan Penting

⚠️ **Keterbatasan:**
- Aplikasi menggunakan **Google Speech Recognition API** yang memerlukan koneksi internet
- Akurasi recognition bergantung pada:
  - Kualitas audio/mikrofon
  - Kejelasan pengucapan
  - Tingkat noise lingkungan
  - Kualitas koneksi internet
- Bahasa yang didukung: **Bahasa Indonesia** saja

💡 **Tips untuk Hasil Terbaik:**
- Gunakan headset atau mikrofon eksternal untuk kualitas audio lebih baik
- Rekam di ruangan yang tenang
- Berbicara dengan kecepatan natural, tidak terlalu cepat atau lambat
- Ucapkan kata dengan jelas dan artikulasi yang baik

---







