import streamlit as st
from PIL import Image
import numpy as np
import os
from tensorflow.keras.models import load_model

# ====== CSS ======
st.markdown("""
    <style>
    .header-scan {
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .section-box {
        background-color: #f4f4f4;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        margin-bottom: 30px;
    }
    .success {
        background-color: #e6ffe6;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid green;
        font-size: 18px;
    }
    .error {
        background-color: #ffe6e6;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid red;
        font-size: 18px;
    }
    .result-box {
        background-color: #e0f7fa;
        padding: 18px;
        border-radius: 12px;
        border-left: 6px solid #00796b;
        font-size: 20px;
        font-weight: bold;
        color: #004d40;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# ====== Judul ======
st.markdown('<div class="header-scan"> Scan Kesegaran Ikan</div>', unsafe_allow_html=True)

# ====== Load Models ======
base_path = os.path.join(os.path.dirname(__file__), '..', 'model')
model_ikan = load_model(os.path.join(base_path, 'model_cek_ikan.h5'))
model_kepala = load_model(os.path.join(base_path, 'model_cek_kepala_ikan.h5'))
model_kesegaran = load_model(os.path.join(base_path, 'model_last_ikan.h5'))

# ====== Fungsi Prediksi Umum ======
def prediksi_model(img, model, threshold, kelas_utama, kelas_tidak):
    img = img.convert("RGB")  # <- penting! pastikan RGB
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = img_array.reshape(1, 224, 224, 3)
    pred = model.predict(img_array)
    skor = pred[0][0]
    hasil = kelas_utama if skor > threshold else kelas_tidak
    return hasil, skor


# ====== Fungsi Alur Prediksi Bertingkat ======
def proses_3_tahap(img):
    # Tahap 1: Cek apakah gambar ikan
    hasil1, skor1 = prediksi_model(img, model_ikan, 0.8, 'ikan', 'bukan_ikan')
    if hasil1 == 'bukan_ikan':
        if st.button("Gambar ini bukan ikan, harap foto/scan gambar ikan, Klik tombol clear atau icon silang pada diatas gambar untuk cek ulang."):
            st.rerun()

        return

    # Tahap 2: Cek apakah kepala ikan
    hasil2, skor2 = prediksi_model(img, model_kepala, 0.8, 'kepala_ikan', 'bukan_kepala')
    if hasil2 == 'bukan_kepala':
        if st.button("Harap berikan gambar seperti panduan yang ada di page cara penggunaan (foto kepala ikan saja),Klik tombol clear pada diatas gambar untuk cek ulang."):
            st.rerun()
        return

    # Tahap 3: Cek kesegaran ikan
    hasil3, skor3 = prediksi_model(img, model_kesegaran, 0.5, 'Tidak Segar', 'Segar')
    st.markdown('<div class="success">✅ Gambar valid. Sistem memproses prediksi kesegaran...</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="result-box">🧪 Hasil Prediksi: <strong>{hasil3}</strong><br>📊 Skor: {skor3:.4f}</div>', unsafe_allow_html=True)

# ====== Pilihan Metode Input ======
metode = st.radio("Pilih Metode Input Gambar", ("📷 Scan Kamera", "📁 Upload File"), horizontal=True)

if metode == "📷 Scan Kamera":
    st.markdown('<div class="section-box">Gunakan kamera untuk mengambil gambar ikan secara langsung.</div>', unsafe_allow_html=True)
    cam_image = st.camera_input("Ambil Gambar")
    if cam_image:
        image = Image.open(cam_image)
        st.image(image, caption="Gambar dari Kamera", use_container_width=True)
        proses_3_tahap(image)

else:
    st.markdown('<div class="section-box">Unggah gambar ikan dengan format <strong>jpg, jpeg, atau png</strong>.</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Pilih File Gambar", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        ekstensi = os.path.splitext(uploaded_file.name)[1].lower()
        if ekstensi not in [".jpg", ".jpeg", ".png"]:
            st.markdown('<div class="error">❌ Format tidak didukung. Harap unggah file jpg, jpeg, atau png.</div>', unsafe_allow_html=True)
        else:
            image = Image.open(uploaded_file)
            st.image(image, caption="Gambar yang Diunggah", use_container_width=True)
            proses_3_tahap(image)

# ====== Catatan Tambahan ======
st.info("📌 *Pastikan fokus gambar pada kepala ikan, khususnya bagian bola mata, agar hasil prediksi lebih akurat, untuk deteksi ulang dengan gambar baru klik icon silang diatas atau click  Browse Files*")
