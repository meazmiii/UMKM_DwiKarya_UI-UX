import streamlit as st
import streamlit.components.v1 as components

# 1. Konfigurasi Halaman (WAJIB di baris pertama setelah import)
st.set_page_config(
    page_title="Dwikarya | Furniture",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. CSS untuk Full Screen & Menghilangkan Padding Streamlit
st.markdown("""
    <style>
        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
        }
        header, footer, #MainMenu {
            visibility: hidden;
            height: 0;
        }
        iframe {
            width: 100vw !important;
            height: 100vh !important;
            border: none;
        }
        .stApp {
            overflow: hidden;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Gabungkan seluruh HTML kamu ke dalam SATU variabel saja agar tidak bingung
html_final = """
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
  </style>
</head>
<body class="text-white bg-black">
    <header class="sticky top-0 left-0 w-full z-30 px-6 md:px-12 py-4 flex justify-between items-center bg-black bg-opacity-60 backdrop-blur">
        <h1 class="text-white font-bold text-xl">DWIKARYA</h1>
        <a class="hover:underline text-xs md:text-sm">(Azmi Aziz 4903, Herlambang Sujatmiko 4925, Raffi Nurzahid 4930)</a>
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
  </section>

  <section id="tentang" class="bg-white text-gray-800 py-16 px-6 md:px-12 text-center">
    <h2 class="text-3xl font-bold mb-6">Tentang Kami</h2>
    <p class="max-w-3xl mx-auto text-lg">
    DWIKARYA adalah produsen dan penyedia furniture modern yang berkomitmen menghadirkan kualitas, keindahan, dan kenyamanan dalam setiap produk. Berdiri sejak 2015, kami telah melayani ribuan pelanggan dari berbagai daerah.
    </p>
  </section>

  <section id="produk" class="bg-gray-100 text-gray-800 py-16 px-6 md:px-12">
    <div class="max-w-6xl mx-auto">
      <h2 class="text-3xl font-bold mb-10 text-center">Produk Terkini Kami</h2>
      <div class="flex flex-wrap justify-center gap-6">
        <div class="w-[250px] bg-white rounded-xl shadow-xl overflow-hidden">
          <img src="https://events.rumah123.com/wp-content/uploads/sites/38/2022/11/03161311/Furniture-Minimalis-Ruang-Tamu-Kayu-Rotan-1024x682.jpg" class="w-full h-48 object-cover" />
          <div class="p-4 text-center">
            <h3 class="text-lg font-bold mb-1">Kursi Modern</h3>
            <p class="text-sm font-bold">Rp. 250.000</p>
          </div>
        </div>
        <div class="w-[250px] bg-white rounded-xl shadow-xl overflow-hidden">
          <img src="https://cdn.scgcbm.id/wp-content/uploads/2023/07/image-22-1024x723.png" class="w-full h-48 object-cover" />
          <div class="p-4 text-center">
            <h3 class="text-lg font-bold mb-1">Lemari Modern</h3>
            <p class="text-sm font-bold">Rp. 1.620.000</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section id="keuntungan" class="bg-white text-gray-800 py-16 px-6 md:px-12 text-center">
    <h2 class="text-3xl font-bold mb-6">Keuntungan Mitra</h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto">
      <div class="p-6 bg-gray-100 rounded-lg shadow-lg"><h3>Tanpa Modal Besar</h3></div>
      <div class="p-6 bg-gray-100 rounded-lg shadow-lg"><h3>Dukungan Penuh</h3></div>
      <div class="p-6 bg-gray-100 rounded-lg shadow-lg"><h3>Keuntungan Menarik</h3></div>
    </div>
  </section>

  <section id="daftar" class="bg-gray-100 py-16 px-6 text-center">
    <div class="max-w-md mx-auto bg-white p-8 rounded-xl shadow-lg text-gray-800">
      <h2 class="text-2xl font-semibold mb-6">Daftar Mitra</h2>
      <form action="https://wa.me/6283876788630" method="get" target="_blank">
        <input type="text" placeholder="Nama Toko" required class="w-full mb-4 px-4 py-2 border rounded-md">
        <button type="submit" class="w-full bg-blue-600 text-white py-3 rounded-full">Kirim via WhatsApp</button>
      </form>
    </div>
  </section>

</body>
</html>
"""

# 4. Tampilkan Hasil Akhir
components.html(html_final, height=3500, scrolling=True)
