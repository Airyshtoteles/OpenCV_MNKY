# 🐵 OpenCV MNKY - Gesture-Controlled Avatar Meme

Interactive real-time gesture recognition system that changes avatar memes based on your hand and face gestures using OpenCV and MediaPipe.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 🎯 **Real-time Face Detection** - Detects your face using MediaPipe
- ✋ **Hand Gesture Recognition** - Tracks hand movements and specific gestures
- 🖼️ **Dynamic Avatar Switching** - Changes avatar based on detected gestures:
  - 😐 **Face only** - Shows one avatar
  - 👋 **Face + Hand** - Shows different avatar
  - 🤫 **Finger near mouth** - Shows special "shh" avatar
- 📹 **External Camera Support** - Works with external cameras (Camo, OBS Virtual Camera, etc.)
- 🖥️ **Fullscreen Mode** - Press `F` for fullscreen experience
- ⚡ **High Performance** - Optimized for smooth real-time processing

## 🎬 Demo

The program displays a split-screen view:
- **Left Side**: Your camera feed (mirrored)
- **Right Side**: Avatar that changes based on your gestures

## 📋 Prerequisites

- Python 3.8 or higher
- Webcam or external camera (e.g., Camo, OBS Virtual Camera)
- Windows / macOS / Linux

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Airyshtoteles/OpenCV_MNKY.git
cd OpenCV_MNKY
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Your Avatar Images

Place three avatar images in the project folder with these names:
- `mon1.jpg` - Avatar for "finger near mouth" gesture
- `mon2.jpg` - Avatar for "face + hand" detection
- `mon3.jpg` - Avatar for "face only" detection

> **Note**: You can use any JPG images. The program will automatically resize them.

### 4. Run the Program

```bash
python meme.py
```

## ⌨️ Controls

| Key | Action |
|-----|--------|
| `ESC` | Exit the program |
| `F` | Toggle fullscreen mode |

## 🎮 How It Works

1. **Face Only**: When only your face is detected, it shows `mon3.jpg`
2. **Face + Hand**: When both face and hand are visible, it shows `mon2.jpg`
3. **Finger Near Mouth**: When you put your finger near your mouth (shh gesture), it shows `mon1.jpg`
4. **No Detection**: Shows a black screen when no face is detected

## 🔧 Configuration

### Camera Selection

The program automatically scans for available cameras (index 1-5) and skips the built-in laptop camera (index 0). If you need to modify this:

```python
# In meme.py, line ~40
for cam_index in range(1, 6):  # Change range as needed
```

### Window Size

Current default: **1920x720** (Full HD)

To change the window size, modify these lines in `meme.py`:

```python
# Avatar size (line ~24)
img_a = cv2.resize(img_a, (640, 720))  # width, height

# Camera frame size (line ~107)
frame_resized = cv2.resize(frame, (1280, 720))  # width, height
```

### Detection Sensitivity

Adjust MediaPipe detection confidence:

```python
# Face detection (line ~35)
face_detection = mp_face.FaceDetection(
    model_selection=0, 
    min_detection_confidence=0.6  # Adjust 0.0-1.0
)

# Hand detection (line ~36)
hands = mp_hands.Hands(
    max_num_hands=2, 
    min_detection_confidence=0.6,  # Adjust 0.0-1.0
    min_tracking_confidence=0.5    # Adjust 0.0-1.0
)
```

## 🐛 Troubleshooting

### Camera Not Found
```
RuntimeError: Tidak bisa membuka kamera Camo
```
**Solution**: 
- Make sure your external camera app (Camo, OBS) is running
- Close other apps that might be using the camera
- Try running with different camera index

### Blank/Black Screen
```
✓ Kamera index X berhasil! but screen is black
```
**Solution**:
- Check if the window is minimized or behind other windows
- Press `F` to toggle fullscreen
- Verify camera permissions in system settings

### Import Errors
```
ModuleNotFoundError: No module named 'cv2'
```
**Solution**:
```bash
pip install --upgrade opencv-contrib-python
pip install --upgrade mediapipe
```

### Numpy Version Conflict
```
tensorflow requires numpy<2.2.0
```
**Solution**:
```bash
pip install "numpy>=1.26.0,<2.2.0"
```

## 📁 Project Structure

```
OpenCV_MNKY/
├── meme.py              # Main application
├── mon1.jpg             # Avatar 1 (finger near mouth)
├── mon2.jpg             # Avatar 2 (face + hand)
├── mon3.jpg             # Avatar 3 (face only)
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── SETUP.md            # Detailed setup guide
├── LICENSE             # MIT License
└── .gitignore          # Git ignore rules
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👏 Acknowledgments

- [OpenCV](https://opencv.org/) - Computer vision library
- [MediaPipe](https://mediapipe.dev/) - ML solutions for face and hand detection
- [TensorFlow](https://www.tensorflow.org/) - Machine learning framework

## 📧 Contact

**Repository**: [https://github.com/Airyshtoteles/OpenCV_MNKY](https://github.com/Airyshtoteles/OpenCV_MNKY)

---

Made with ❤️ and 🐵 by [Airyshtoteles](https://github.com/Airyshtoteles)
