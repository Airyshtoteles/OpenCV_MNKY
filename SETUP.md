# 🔧 Detailed Setup Guide - OpenCV MNKY

This guide provides step-by-step instructions for setting up OpenCV MNKY on different operating systems.

## 📑 Table of Contents

- [Windows Setup](#windows-setup)
- [macOS Setup](#macos-setup)
- [Linux Setup](#linux-setup)
- [Using External Cameras](#using-external-cameras)
- [Common Issues](#common-issues)

---

## 🪟 Windows Setup

### Prerequisites

1. **Install Python 3.8+**
   - Download from [python.org](https://www.python.org/downloads/)
   - ✅ Check "Add Python to PATH" during installation

2. **Verify Installation**
   ```powershell
   python --version
   pip --version
   ```

### Installation Steps

1. **Clone the Repository**
   ```powershell
   git clone https://github.com/Airyshtoteles/OpenCV_MNKY.git
   cd OpenCV_MNKY
   ```

2. **Create Virtual Environment (Recommended)**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install Dependencies**
   ```powershell
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Add Avatar Images**
   - Copy your 3 avatar images (JPG format) to the project folder
   - Rename them as: `mon1.jpg`, `mon2.jpg`, `mon3.jpg`

5. **Run the Program**
   ```powershell
   python meme.py
   ```

### Using Camo (iPhone as Webcam)

1. Install [Camo Studio](https://reincubate.com/camo/) on Windows
2. Install Camo app on your iPhone
3. Connect iPhone via USB or WiFi
4. Run the program - it will auto-detect Camo as camera index 1

---

## 🍎 macOS Setup

### Prerequisites

1. **Install Homebrew** (if not already installed)
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python 3.8+**
   ```bash
   brew install python@3.10
   ```

3. **Verify Installation**
   ```bash
   python3 --version
   pip3 --version
   ```

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Airyshtoteles/OpenCV_MNKY.git
   cd OpenCV_MNKY
   ```

2. **Create Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Grant Camera Permissions**
   - System Preferences → Security & Privacy → Camera
   - Allow Terminal or your IDE to access the camera

5. **Add Avatar Images**
   - Copy 3 avatar images to the project folder
   - Rename as: `mon1.jpg`, `mon2.jpg`, `mon3.jpg`

6. **Run the Program**
   ```bash
   python meme.py
   ```

---

## 🐧 Linux Setup

### Prerequisites (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
sudo apt install libgl1-mesa-glx libglib2.0-0
```

### Prerequisites (Fedora/RHEL)

```bash
sudo dnf install python3 python3-pip
sudo dnf install mesa-libGL glib2
```

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Airyshtoteles/OpenCV_MNKY.git
   cd OpenCV_MNKY
   ```

2. **Create Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Configure Camera Permissions**
   ```bash
   # Add your user to video group
   sudo usermod -a -G video $USER
   # Log out and log back in for changes to take effect
   ```

5. **Add Avatar Images**
   ```bash
   # Copy your images
   cp /path/to/your/image1.jpg ./mon1.jpg
   cp /path/to/your/image2.jpg ./mon2.jpg
   cp /path/to/your/image3.jpg ./mon3.jpg
   ```

6. **Run the Program**
   ```bash
   python meme.py
   ```

---

## 📹 Using External Cameras

### Camo (iPhone/Android as Webcam)

**Windows:**
1. Install Camo Studio
2. Connect phone via USB/WiFi
3. Run the program (auto-detects as index 1)

**macOS:**
1. Install Camo from App Store
2. Grant camera permissions
3. Run the program

### OBS Virtual Camera

1. Install [OBS Studio](https://obsproject.com/)
2. Start Virtual Camera in OBS
3. Run the program
4. If not detected, modify camera index in `meme.py`:
   ```python
   for cam_index in range(1, 10):  # Increase range
   ```

### DroidCam (Android as Webcam)

1. Install [DroidCam](https://www.dev47apps.com/)
2. Connect via USB or WiFi
3. Run the program

---

## 🐛 Common Issues

### Issue 1: Module Not Found

```
ModuleNotFoundError: No module named 'cv2'
```

**Solution:**
```bash
pip uninstall opencv-python opencv-contrib-python -y
pip install opencv-contrib-python==4.12.0.88
```

---

### Issue 2: Numpy Version Conflict

```
tensorflow requires numpy<2.2.0, but you have numpy 2.2.6
```

**Solution:**
```bash
pip install "numpy>=1.26.0,<2.2.0"
```

---

### Issue 3: Camera Not Detected

```
RuntimeError: Tidak bisa membuka kamera
```

**Solution:**
1. Check camera is connected
2. Close other apps using camera (Zoom, Teams, etc.)
3. Try different camera index:
   ```python
   # Modify in meme.py
   for cam_index in range(0, 10):  # Try more indexes
   ```

---

### Issue 4: Blank/Black Window

**Solution:**
1. Check if window is behind other windows
2. Press `F` for fullscreen
3. Verify camera permissions
4. Test camera with other apps first

---

### Issue 5: Low FPS / Laggy

**Solutions:**
1. Reduce window size in `meme.py`:
   ```python
   img_a = cv2.resize(img_a, (320, 480))  # Smaller size
   frame_resized = cv2.resize(frame, (640, 480))
   ```

2. Lower detection confidence:
   ```python
   face_detection = mp_face.FaceDetection(
       min_detection_confidence=0.5  # Lower = faster
   )
   ```

3. Reduce max hands:
   ```python
   hands = mp_hands.Hands(max_num_hands=1)  # Track 1 hand instead of 2
   ```

---

### Issue 6: Permission Denied (Linux)

```
VIDIOC_REQBUFS: Permission denied
```

**Solution:**
```bash
sudo usermod -a -G video $USER
# Then log out and log back in
```

---

## 🎯 Performance Tips

1. **Use External Camera with Good Lighting** - Better detection accuracy
2. **Close Background Apps** - More CPU for processing
3. **Adjust Window Size** - Smaller = faster
4. **Use Virtual Environment** - Avoid dependency conflicts
5. **Update GPU Drivers** - Better TensorFlow performance

---

## 🆘 Still Having Issues?

1. Check [GitHub Issues](https://github.com/Airyshtoteles/OpenCV_MNKY/issues)
2. Create a new issue with:
   - Your OS and Python version
   - Error message (full traceback)
   - Steps you've tried

---

## 📚 Additional Resources

- [OpenCV Documentation](https://docs.opencv.org/)
- [MediaPipe Documentation](https://google.github.io/mediapipe/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

---

**Happy Coding!** 🐵✨
