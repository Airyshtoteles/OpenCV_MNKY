import cv2
import mediapipe as mp
import numpy as np
import os

print("Current working directory:", os.getcwd())

# --- Load gambar avatar ---
img_a = cv2.imread("mon2.jpg")
img_b = cv2.imread("mon3.jpg")
img_c = cv2.imread("mon1.jpg")

# --- Debug print untuk cek gambar ---
print("Image A:", "OK" if img_a is not None else "FAILED")
print("Image B:", "OK" if img_b is not None else "FAILED")
print("Image C:", "OK" if img_c is not None else "FAILED")

# --- Pastikan semua gambar terbaca sebelum resize ---
# Gunakan pemeriksaan identitas agar tidak memicu perbandingan array numpy yang ambigu
if any(x is None for x in (img_a, img_b, img_c)):
    raise FileNotFoundError("❌ Salah satu gambar gagal dibaca! Cek nama file & formatnya di folder ini.")

# --- Resize agar seragam (ukuran BESAR untuk fullscreen) ---
# Format: (width, height) - ukuran 720p
img_a = cv2.resize(img_a, (640, 720))
img_b = cv2.resize(img_b, (640, 720))
img_c = cv2.resize(img_c, (640, 720))

"""
Setup Mediapipe Face Detection & Hands
"""
# Inisialisasi modul solusi yang benar
mp_face = mp.solutions.face_detection
mp_hands = mp.solutions.hands

# Buat instance detektor wajah dan tangan
face_detection = mp_face.FaceDetection(model_selection=0, min_detection_confidence=0.6)
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.6, min_tracking_confidence=0.5)

# Inisialisasi kamera - skip index 0, coba 1-5 untuk Camo
cap = None
for cam_index in range(0, 6):  # Coba index 1-5, skip 0 (kamera laptop rusak)
    print(f"Mencoba membuka kamera index {cam_index}...")
    test_cap = cv2.VideoCapture(cam_index, cv2.CAP_DSHOW)  # CAP_DSHOW untuk Windows
    if test_cap.isOpened():
        ret, test_frame = test_cap.read()
        if ret and test_frame is not None:
            print(f"✓ Kamera index {cam_index} berhasil! Resolusi: {test_frame.shape[1]}x{test_frame.shape[0]}")
            cap = test_cap
            break
        else:
            test_cap.release()
    
if cap is None or not cap.isOpened():
    raise RuntimeError("Tidak bisa membuka kamera Camo. Pastikan Camo running dan tidak dipakai app lain.")

print("Mulai loop video... Tekan ESC untuk keluar, F untuk fullscreen toggle")
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Gagal membaca frame dari kamera!")
        break
    
    frame_count += 1
    if frame_count == 1:
        print(f"✓ Frame pertama berhasil dibaca! Ukuran: {frame.shape}")

    # Balik tampilan kamera biar mirror
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Convert ke RGB untuk Mediapipe
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Deteksi wajah & tangan
    face_result = face_detection.process(frame_rgb)
    hand_result = hands.process(frame_rgb)

    face_detected = face_result.detections is not None
    hand_detected = hand_result.multi_hand_landmarks is not None
    finger_near_mouth = False

    # Jika ada wajah dan tangan, cek posisi jari ke bibir
    if face_detected and hand_detected:
        for detection in face_result.detections:
            # Dapatkan posisi wajah (khususnya bibir)
            bboxC = detection.location_data.relative_bounding_box
            mouth_y = (bboxC.ymin + bboxC.height * 0.75) * h  # kira-kira posisi bibir

        for hand_landmarks in hand_result.multi_hand_landmarks:
            # Titik ujung telunjuk (index finger tip)
            finger_tip = hand_landmarks.landmark[8]
            finger_y = finger_tip.y * h
            finger_x = finger_tip.x * w

            # Cek apakah jari dekat bibir
            if abs(finger_y - mouth_y) < 40:
                finger_near_mouth = True

    # Tentukan avatar mana yang ditampilkan
    if face_detected and finger_near_mouth:
        avatar = img_c  # jari di bibir
    elif face_detected and hand_detected:
        avatar = img_a  # ada wajah + tangan
    elif face_detected:
        avatar = img_b  # hanya wajah
    else:
        # Jika tidak ada wajah, tampilkan layar hitam di kanan
        avatar = np.zeros((720, 640, 3), dtype=np.uint8)

    # Resize frame kamera biar sejajar dengan avatar (ukuran BESAR 720p)
    # Format: (width, height) - tinggi harus sama dengan avatar (720)
    frame_resized = cv2.resize(frame, (1280, 720))

    # Gabungkan dua tampilan (kamera kiri, avatar kanan)
    # Total window size: 1920x720 (Full HD width, 720p height)
    combined = np.hstack((frame_resized, avatar))

    # Tampilkan hasil - set window ke FULLSCREEN atau NORMAL dengan size besar
    cv2.namedWindow("Gesture Avatar", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Gesture Avatar", 1920, 720)
    cv2.imshow("Gesture Avatar", combined)

    # Kontrol keyboard
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC untuk keluar
        break
    elif key == ord('f') or key == ord('F'):  # F untuk fullscreen toggle
        cv2.setWindowProperty("Gesture Avatar", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Tutup semua
cap.release()
cv2.destroyAllWindows()
