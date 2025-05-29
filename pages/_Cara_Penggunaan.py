import streamlit as st

# Tambahkan CSS untuk memperbesar teks
st.markdown("""
    <style>
    .cara-penggunaan {
        font-size: 22px;
        line-height: 1.8;
    }
    .cara-penggunaan strong {
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)

# Judul besar
st.markdown('<h1 style="font-size: 42px;">🧾 Cara Penggunaan</h1>', unsafe_allow_html=True)

# Isi instruksi
st.markdown("""
<div class="cara-penggunaan">
1. Buka menu <strong>Scan</strong> di sidebar.<br>
2. Pilih metode input: ambil gambar langsung atau upload gambar ikan dengan format yang disarankan yaitu <strong>jpg, jpeg, dan png</strong>.<br>
3. Setelah gambar berhasil dimasukkan, sistem akan memproses dan memberikan hasil prediksi kesegaran untuk menentukan ikan segar atau tidak.<br>
4. Pastikan arah kamera atau file fokus kepada <strong>kepala ikan</strong> khususnya pada bagian <strong>bola mata</strong>.<br>
5. Hasilnya akan ditampilkan secara instan di layar.<br><br>
<strong>Catatan:</strong> Pastikan gambar jelas dan tidak buram agar hasil lebih akurat, perhatikan contoh dibawah ini !
</div>
""", unsafe_allow_html=True)

# Gambar menggunakan st.image agar tampil dari folder lokal
st.image("geleri/a.jpg", caption="Contoh gambar ikan yang benar", width=640)
