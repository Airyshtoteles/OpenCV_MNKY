# 📸 OpenCV AI Meme & Gesture Detector

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Face%20%26%20Hand-orange)

Aplikasi Computer Vision real-time yang menggunakan **OpenCV** dan **MediaPipe** untuk mendeteksi wajah, tangan, dan gestur spesifik (seperti gestur "Shh" 🤫). Program ini juga menampilkan overlay gambar (meme) berdasarkan interaksi pengguna.

![Demo Preview](images/demo.gif)
*(Pastikan kamu sudah upload file demo.gif ke folder images)*

## ✨ Fitur Utama

- **Real-time Face Detection**: Mendeteksi wajah pengguna secara akurat.
- **Hand Tracking**: Melacak pergerakan tangan dan jari (Landmarks).
- **Gesture Recognition**:
  - Mendeteksi gestur jari telunjuk di dekat mulut (Shh/Diam).
  - Logika deteksi interaktif antara posisi tangan dan wajah.
- **Meme Overlay**: Menampilkan aset gambar (`mon1.jpg`, `jaja.jpg`, dll) ke layar.

## 📂 Struktur Folder

```text
.
├── images/             # Folder aset gambar dokumentasi
│   ├── demo.gif
│   ├── screenshot-main.png
│   └── ...
├── meme.py             # Main source code (Logic OpenCV & MediaPipe)
├── requirements.txt    # Daftar library yang dibutuhkan
├── mon1.jpg             # Aset overlay
└── README.md           # Dokumentasi proyek ini