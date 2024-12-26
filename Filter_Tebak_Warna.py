import cv2
import mediapipe as mp
import time
import random

# Inisialisasi MediaPipe Face Detection
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Warna campuran dan jawaban
def generate_questions():
    return [
        {"question": "Kuning + Biru", "options": random.sample(["Hijau", "Orange"], 2), "answer": "Hijau"},
        {"question": "Merah + Kuning", "options": random.sample(["Orange", "Ungu"], 2), "answer": "Orange"},
        {"question": "Merah + Biru", "options": random.sample(["Ungu", "Hijau"], 2), "answer": "Ungu"},
        {"question": "Biru + Hijau", "options": random.sample(["Cyan", "Ungu"], 2), "answer": "Cyan"},
        {"question": "Kuning + Hijau", "options": random.sample(["Lime", "Merah"], 2), "answer": "Lime"},
        {"question": "Cyan + Kuning", "options": random.sample(["Lime", "Hijau"], 2), "answer": "Hijau"},
        {"question": "Merah + Hijau", "options": random.sample(["Kuning", "Cokelat"], 2), "answer": "Cokelat"},
        {"question": "Merah + Hijau", "options": random.sample(["Kuning", "Orange"], 2), "answer": "Kuning"},
        {"question": "Biru + Merah", "options": random.sample(["Magenta", "Cokelat"], 2), "answer": "Magenta"},
        {"question": "Kuning + Magenta", "options": random.sample(["Hijau", "Orange"], 2), "answer": "Orange"}
    ]

questions = generate_questions()

# Fungsi untuk menampilkan hasil
def display_result(frame, result_text):
    cv2.putText(frame, result_text, (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 4)

# Fungsi untuk menampilkan pertanyaan tanpa latar belakang
def display_question(frame, text, position, text_color):
    cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 2)

# Inisialisasi kamera
cap = cv2.VideoCapture(0)

current_question = None
score = 0
start_time = time.time()
time_limit = 7
last_answer_time = 0  # Waktu terakhir jawaban diberikan
question_delay = 3  # Jeda antar pertanyaan
question_count = 0
max_questions = 10

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb_frame)

    # Menampilkan pertanyaan jika tidak ada pertanyaan aktif dan ada cukup waktu jeda
    if not current_question and time.time() - last_answer_time >= question_delay and question_count < max_questions:
        questions = generate_questions()
        current_question = random.choice(questions)
        start_time = time.time()
        question_count += 1

    # Menampilkan pertanyaan dan pilihan jawaban
    if current_question:
        display_question(frame, current_question["question"], (w // 2 - 150, 50), (0, 0, 0))  # Pertanyaan di tengah atas
        display_question(frame, f"{current_question['options'][0]}", (50, h // 2), (0, 0, 0))  # Jawaban kiri di sebelah kiri kepala
        display_question(frame, f"{current_question['options'][1]}", (w - 200, h // 2), (0, 0, 0))  # Jawaban kanan di sebelah kanan kepala

    if result.multi_face_landmarks:
        for face_landmarks in result.multi_face_landmarks:
            # Mengambil posisi landmark untuk mendeteksi arah kepala
            nose_tip = face_landmarks.landmark[1]  # Indeks landmark hidung (nose_tip)

            x = int(nose_tip.x * w)

            if x < w // 3:  # Kepala ke kiri
                if current_question:
                    selected_option = current_question["options"][0]
                    if selected_option == current_question["answer"]:
                        display_result(frame, "Benar")
                        score += 1
                    else:
                        display_result(frame, "Salah")
                current_question = None
                last_answer_time = time.time()

            elif x > (w * 2) // 3:  # Kepala ke kanan
                if current_question:
                    selected_option = current_question["options"][1]
                    if selected_option == current_question["answer"]:
                        display_result(frame, "Benar")
                        score += 1
                    else:
                        display_result(frame, "Salah")
                current_question = None
                last_answer_time = time.time()

    # Cek batas waktu untuk satu pertanyaan
    if time.time() - start_time > time_limit and current_question:
        current_question = None
        last_answer_time = time.time()

    # Menampilkan skor
    cv2.putText(frame, f"Skor: {score}", (w // 2 - 100, h - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)  # Skor di bawah kepala

    # Menampilkan video
    cv2.imshow('Quiz Game', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Menghentikan permainan setelah 10 pertanyaan
    if question_count >= max_questions:
        break

cap.release()
time.sleep(5)  # Jeda 5 detik sebelum menutup semua jendela
cv2.destroyAllWindows()
