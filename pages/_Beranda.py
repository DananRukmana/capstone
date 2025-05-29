import streamlit as st
from streamlit.components.v1 import html


# Gaya CSS kustom untuk estetika yang lebih besar + posisi tombol di atas
st.markdown("""
    <style>
    .main-title {
        font-size: 48px;
        font-weight: 800;
        color: #004e89;
        text-align: center;
        margin-top: 50px;
    }
    .subtitle {
        font-size: 24px;
        color: #333;
        text-align: center;
        margin-bottom: 40px;
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
    }
    .feature-box {
        background-color: #f0f8ff;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 4px 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 40px;
        font-size: 20px;
        line-height: 1.6;
        max-width: 1000px;
        margin-left: auto;
        margin-right: auto;
    }
    .feature-title {
        font-size: 24px;
        font-weight: bold;
        color: #004e89;
        margin-bottom: 10px;
    }
    .scan-button {
        display: flex;
        justify-content: center;
        margin-top: -150px; /* Naikkan ke atas sekitar 4cm */
        margin-bottom: 50px;
    }
    .stButton>button {
        background-color: #004e89;
        color: white;
        font-size: 20px;
        font-weight: bold;
        padding: 14px 32px;
        border-radius: 10px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #0066cc;
        transition: 0.3s;
    }
    </style>
""", unsafe_allow_html=True)

# Judul utama
st.markdown('<div class="main-title">Segarikan</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Sistem Pendeteksi Kesegaran Ikan Untuk Kelayakan Konsumsi Guna Mendukung Keamanan Pangan Berbasis Website</div>', unsafe_allow_html=True)

# Penjelasan singkat
st.markdown("""
<style>
.feature-box p {
    text-align: justify;
}
</style>

<div class="feature-box">
    <p>
        <strong>Segarikan</strong> adalah aplikasi berbasis web yang dirancang untuk membantu masyarakat dalam mengklasifikasikan kesegaran ikan berdasarkan gambar. 
        Tujuannya adalah untuk mendukung keamanan pangan, mengurangi limbah makanan, dan menjaga keberlanjutan lingkungan. 
        Dengan teknologi machine learning, pengguna dapat dengan cepat mengetahui apakah ikan layak dikonsumsi atau tidak.
    </p>
</div>
""", unsafe_allow_html=True)

# Fitur-fitur lainnya
st.markdown("""
<div class="feature-box">
    <div class="feature-title">📌 Fitur Utama</div>
    <ul>
        <li><strong>Scan dan Upload</strong>: Deteksi kesegaran ikan dengan upload gambar.</li>
        <li><strong>Cara Penggunaan</strong>: Panduan lengkap langkah demi langkah.</li>
        <li><strong>Kontak</strong>: Hubungi kami untuk bantuan dan saran.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Tombol scan
st.markdown('<div class="scan-button">', unsafe_allow_html=True)
if st.button("🔍 Mulai Scan Ikan"):
    st.switch_page("pages/_Scan.py")
st.markdown('</div>', unsafe_allow_html=True)
