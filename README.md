# Cari Biodata Mahasiswa melalui Web Scraping

Proyek ini adalah aplikasi berbasis **Flask** yang memungkinkan pengguna mencari biodata mahasiswa berdasarkan **Nomor Pokok Mahasiswa (NPM)** melalui metode **Web Scraping** dari situs **PDDikti**.

## 🚀 Fitur Utama

- Menginput **NPM mahasiswa** untuk pencarian.
- Mengambil data dari **PDDikti** melalui teknik **Web Scraping** menggunakan **Selenium & BeautifulSoup**.
- Menampilkan hasil pencarian dalam tampilan web dengan desain **Bootstrap**.
- Menangani file PDF (jika dikembangkan lebih lanjut) untuk pencarian NPM massal.

---

## 🛠 Instalasi & Persiapan

### 1️⃣ **Kloning Repository** (Jika menggunakan Git)

```sh
git clone https://github.com/username/proyek-pddikti-scraper.git
cd proyek-pddikti-scraper
```

### 2️⃣ **Buat Virtual Environment & Instal Dependensi**

```sh
python -m venv venv
source venv/bin/activate  # (Mac/Linux)
venv\Scripts\activate  # (Windows)
pip install -r requirements.txt
```

### 3️⃣ **Install ChromeDriver (Selenium)**

```sh
pip install webdriver-manager
```

---

## ⚡ Cara Menjalankan

Jalankan aplikasi Flask dengan perintah berikut:

```sh
python app.py
```

Aplikasi akan berjalan di **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## 📜 Teknologi yang Digunakan

- **Python** (Flask, Selenium, BeautifulSoup, WebDriver Manager)
- **HTML + Bootstrap** (Antarmuka web yang responsif)
- **Web Scraping** (Mengambil data langsung dari situs PDDikti)

---

## 📌 Struktur Folder

```
📂 proyek-pddikti-scraper
│── app.py                # Main Flask App
│── templates/
│   ├── index.html        # Tampilan web
│── requirements.txt      # Daftar dependensi
│── README.md             # Dokumentasi ini
```

---

## 📩 Catatan Penting

- **Pastikan koneksi internet stabil**, karena scraping bergantung pada kecepatan akses ke situs PDDikti.
- **Gunakan User-Agent dalam Selenium** untuk menghindari deteksi bot.
- **Jika scraping gagal**, coba debug dengan menyimpan halaman hasil scraping (`debug.html`).

---

## 🎯 Pengembangan ke Depan

✅ **Menambahkan fitur upload PDF** untuk mencari NPM secara massal.
✅ **Integrasi API PDDikti jika tersedia** untuk hasil lebih cepat.
✅ **Logging dan Error Handling** agar lebih robust.

---

💡 **Kontribusi & Saran?** Jangan ragu untuk membuat *pull request* atau *issue* di repository ini!

🔗 **Dibuat oleh:** [Rahmat Mulia] 
