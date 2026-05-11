import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Dwikarya | Furniture",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
    <style>
        .block-container { padding: 0rem !important; max-width: 100% !important; }
        header, footer, #MainMenu { visibility: hidden; height: 0; }
        iframe { width: 100vw !important; height: 100vh !important; border: none; }
        .stApp { overflow: hidden; }
    </style>
""", unsafe_allow_html=True)

html_final = """
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
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
        <nav class="space-x-4 text-sm md:text-base">
            <a href="#produk" class="nav-link hover:underline">Produk</a>
            <a href="#tentang" class="nav-link hover:underline">Tentang Kami</a>
            <a href="#keuntungan" class="nav-link hover:underline">Keuntungan</a>
            <a href="#daftar" class="nav-link hover:underline">Daftar</a>
        </nav>
    </header>

  <section class="relative h-screen bg-cover bg-center" style="background-image: url('https://www.woodleys.com/blog/wp-content/uploads/sites/105/2022/02/8-Living-Room-Furniture-Ideas-for-Your-New-Home.jpg');">
    <div class="absolute inset-0 bg-black bg-opacity-60"></div>
    <div class="relative z-10 max-w-7xl mx-auto h-full flex flex-col justify-center px-6 md:px-12">
      <div class="w-full md:w-1/2">
        <h1 class="text-4xl md:text-5xl font-bold mb-4">DWIKARYA</h1>
        <p class="mb-6 text-lg">Pilihan terbaik untuk Furniture Anda.</p>
        <a href="https://wa.me/6283876788630" target="_blank" class="bg-white text-blue-600 font-semibold px-6 py-3 rounded-full">PESAN DISINI</a>
      </div>
    </div>
  </section>

  <section id="tentang" class="bg-white text-gray-800 py-16 px-6 md:px-12 text-center">
    <h2 class="text-3xl font-bold mb-6">Tentang Kami</h2>
    <p class="max-w-3xl mx-auto text-lg">DWIKARYA adalah produsen furniture modern berkualitas...</p>
  </section>

  <section id="produk" class="bg-gray-100 text-gray-800 py-16 px-6 md:px-12">
    <h2 class="text-3xl font-bold mb-10 text-center">Produk Terkini</h2>
    <div class="flex flex-wrap justify-center gap-6">
        <div class="w-[250px] bg-white rounded-xl shadow-xl overflow-hidden p-4">
            <img src="https://events.rumah123.com/wp-content/uploads/sites/38/2022/11/03161311/Furniture-Minimalis-Ruang-Tamu-Kayu-Rotan-1024x682.jpg" class="rounded-lg">
            <h3 class="font-bold mt-2">Kursi Modern</h3>
        </div>
    </div>
  </section>

  <section id="keuntungan" class="bg-white text-gray-800 py-16 px-6 md:px-12 text-center">
    <h2 class="text-3xl font-bold mb-6">Keuntungan</h2>
    <p>Dukungan penuh dan tanpa modal besar.</p>
  </section>

  <section id="daftar" class="bg-gray-100 py-16 px-6">
    <div class="max-w-md mx-auto bg-white p-8 rounded-xl shadow-lg text-gray-800">
      <h2 class="text-2xl font-bold mb-6 text-center">Formulir Mitra</h2>
      <form action="https://wa.me/6283876788630" target="_blank">
        <input type="text" placeholder="Nama Store" class="w-full mb-4 px-4 py-2 border rounded-md">
        <button type="submit" class="w-full bg-blue-600 text-white py-3 rounded-full">Daftar</button>
      </form>
    </div>
  </section>

  <script>
    document.querySelectorAll('.nav-link').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
  </script>
</body>
</html>
"""

components.html(html_final, height=4500, scrolling=True)
