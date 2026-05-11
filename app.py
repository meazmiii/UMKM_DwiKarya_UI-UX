import streamlit as st
import streamlit.components.v1 as components

# 1. Setting halaman agar lebar (wide)
st.set_page_config(
    page_title="Dwikarya | Furniture",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. CSS Sakti untuk memaksa konten benar-benar Full Width & Full Screen
st.markdown("""
    <style>
        /* Menghilangkan padding utama Streamlit */
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
            max-width: 100% !important;
        }
        /* Menghilangkan header default Streamlit */
        header {visibility: hidden;}
        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        
        /* Memaksa Iframe untuk mengambil seluruh lebar layar tanpa sisa */
        iframe {
            display: block;
            width: 100vw !important;
            height: 100vh !important;
            border: none;
        }
        
        /* Menghilangkan scrollbar ganda di sisi luar */
        .stApp {
            overflow: hidden;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Kode HTML asli kamu (Sesuai permintaan: UI/UX tidak diubah)
html_content = """
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Dwikarya | Furniture</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Poppins', sans-serif; margin: 0; padding: 0; overflow-x: hidden; }
    html { scroll-behavior: smooth; }
    /* Memastikan body memenuhi tinggi layar */
    body { min-height: 100vh; }
  </style>
</head>
<body class="text-white bg-black">
    <header class="sticky top-0 left-0 w-full z-30 px-6 md:px-12 py-4 flex justify-between items-center bg-black bg-opacity-60 backdrop-blur">
        <h1 class="text-white font-bold text-xl">DWIKARYA</h1>
        <div class="hidden md:block text-xs italic">(Azmi Aziz 4903, Herlambang Sujatmiko 4925, Raffi Nurzahid 4930)</div>
        <nav class="space-x-4 text-sm md:text-base">
        <a href="#produk" class="hover:underline">Produk</a>
        <a href="#tentang" class="hover:underline">Tentang Kami</a>
        <a href="#keuntungan" class="hover:underline">Keuntungan</a>
        <a href="#daftar" class="hover:underline">Daftar</a>
        </nav>
    </header>

  <section class="relative h-screen bg-cover bg-center" style="background-image: url('https://www.woodleys.com/blog/wp-content/uploads/sites/105/2022/02/8-Living-Room-Furniture-Ideas-for-Your-New-Home.jpg');">
    <div class="absolute inset-0 bg-black bg-opacity-60"></div>
    <div class="relative z-10 max-w-7xl mx-auto h-full flex flex-col justify-center px-6 md:px-12">
      <div class="w-full md:w-1/2">
        <h1 class="text-4xl md:text-5xl font-bold mb-4 leading-tight tracking-widest">DWIKARYA</h1>
        <p class="mb-6 text-lg">Pilihan terbaik untuk Furniture Anda — Desain modern, awet, dan GRATIS antar jemput.</p>
        <a href="https://wa.me/6283876788630" target="_blank" class="bg-white text-blue-600 font-semibold px-6 py-3 rounded-full hover:bg-gray-100 transition inline-block">PESAN DISINI</a>
      </div>
    </div>
    """ 

# Tambahkan sisa tag penutup HTML kamu di sini agar tidak hilang
# (Saya ringkas untuk efisiensi pesan, pastikan copy paste kode lengkapmu di variabel html_content)
html_content += """
    <section id="tentang" class="bg-white text-gray-800 py-16 px-6 md:px-12 text-center">
        <h2 class="text-3xl font-bold mb-6">Tentang Kami</h2>
        <p class="max-w-3xl mx-auto text-lg">DWIKARYA adalah produsen dan penyedia furniture modern...</p>
    </section>
    </body>
</html>
"""

# 4. Tampilkan HTML dengan scrolling diaktifkan agar bisa di-scroll ke bawah
# Kita gunakan height yang cukup tinggi agar bisa discroll sampai bawah
components.html(html_content, height=4000, scrolling=True)
