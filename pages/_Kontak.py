import streamlit as st

# CSS untuk layout rapih tanpa tabel
st.markdown("""
    <style>
    .kontak-header {
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .kontak-container {
        font-size: 22px;
        background-color: #f9f9f9;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }
    .row {
        display: flex;
        margin-bottom: 10px;
    }
    .label {
        width: 160px;
        font-weight: bold;
    }
    .value {
        flex: 1;
    }
    </style>
""", unsafe_allow_html=True)

# Judul
st.markdown('<div class="kontak-header">📬 Kontak</div>', unsafe_allow_html=True)

# Isi kontak
st.markdown("""
<div class="kontak-container">
  <div class="row"><div class="label">Nama:</div><div class="value">Danan Rukmana</div></div>
  <div class="row"><div class="label">Universitas:</div><div class="value">Universitas Teuku Umar</div></div>
  <div class="row"><div class="label">Jurusan:</div><div class="value">Teknologi Informasi</div></div>
  <div class="row"><div class="label">Email:</div><div class="value">gmgdanan@gmail.com</div></div>
  <div class="row"><div class="label">Alamat:</div><div class="value">Aceh Singkil, Aceh</div></div>
  <div class="row"><div class="label">LinkedIn:</div><div class="value"><a href="https://www.linkedin.com/in/danan-rukmana" target="_blank">Danan Rukmana</a></div></div>
  <br>
  Terima kasih telah menggunakan aplikasi <strong>Segarikan!</strong>
</div>
""", unsafe_allow_html=True)
