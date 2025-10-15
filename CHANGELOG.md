# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2025-10-15

### Added
- Initial release
- Real-time face detection using MediaPipe
- Hand gesture recognition
- Dynamic avatar switching based on gestures
- Support for external cameras (Camo, OBS Virtual Camera)
- Fullscreen mode toggle (F key)
- Automatic camera detection (skips broken built-in camera)
- High-resolution display (1920x720)
- Mirror mode for natural interaction

### Features
- Three gesture modes:
  - Face only detection
  - Face + hand detection
  - Finger near mouth detection
- Auto-resizing of avatar images
- Debug logging for camera detection
- ESC key to exit gracefully

### Technical
- Python 3.8+ support
- OpenCV 4.12.0.88
- MediaPipe 0.10.14
- TensorFlow 2.19.0 backend
- Windows DirectShow camera support
