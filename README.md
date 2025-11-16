# 📰 Crawler & Scraper Berita Bisnis.com

> “Sebuah pipeline data engineering end-to-end yang dibuat untuk melakukan crawl dan scrape artikel berita dari portal bisnis.com”

---

## 🧩 Project Overview
Proyek ini adalah crawler dan scraper Python yang dirancang untuk mengambil artikel berita dari bisnis.com menggunakan library Beautifulsoup4

Arsitektur proyek ini bersifat modular, memisahkan logika inti Scraper (yang mengambil detail satu artikel) dari Crawler (yang menemukan link artikel). Proyek ini memiliki dua mode eksekusi (entrypoint) yang berbeda sesuai kebutuhan.


## ⚙️ Penjelasan Program
1. Standard Mode (crawl_standard.py):
    a) Berperan sebagai crawler yang dapat dijadwalkan secara berkala untuk mengambil artikel terbaru.
    b) Memulai crawling dari halaman indeks utama (https://www.bisnis.com/index).
    c) Secara otomatis menangani paginasi (halaman ganda) untuk menemukan semua artikel terbaru.
    d) Menyimpan hasilnya sebagai hasil_scraping_standard.json.

2. Backtrack Mode (crawl_backtrack.py):
    a)Menerima parameter start_date dan end_date (saat ini di-hardcode di dalam skrip).
    b)Melakukan looping untuk setiap tanggal dalam rentang tersebut.
    c)Mengunjungi halaman indeks spesifik per tanggal (misal: .../index?date=YYYY-MM-DD).
    d)Menangani paginasi di setiap halaman indeks tanggal untuk memastikan semua artikel terambil.
    e)Menyimpan hasilnya sebagai file JSON dinamis, misal backtrack_20251115_20251116.json.

---

## 🧱 Repository Structure
bisnis-com-crawler/
│
├── scrapers.py             # MODUL DASAR: Berisi fungsi scrape_article_details() 
├── crawl_standard.py       # ENTRYPOINT 1: Mode Standard (Berita Terbaru) [cite: 39, 48]
├── crawl_backtrack.py      # ENTRYPOINT 2: Mode Backtrack (Rentang Tanggal) [cite: 37, 48]
│
├── requirements.txt        # Daftar library yang dibutuhkan
├── .gitignore              # (Direkomendasikan) Untuk mengabaikan .json dan venv
└── README.md               # File ini


---

## 🧰 Teknologi yang dipakai
- **Python**
- **Library yang dipakai:**:
    1) *Requests*: Untuk mengirim permintaan HTTP ke bisnis.com.
    2) *BeautifulSoup4*: Untuk mem-parsing HTML dan mengekstrak data.
    3) *Datetime*: Untuk menangani, mem-parsing, dan memformat tanggal.
    4) *JSON*: Untuk mengekspor data yang telah di-scrape.

- **Arsitektur & Fitur:** Text preprocessing, tokenization, normalization
    1) *Modular*: Logika scraper dan crawler terpisah.
    2) *Error Handling*: Secara tangguh melewati artikel premium/berbayar tanpa crash.
    3) *Data Parsing*: Termasuk logika parser kustom untuk mengonversi format tanggal bahasa Indonesia ("Jumat, 14 November 2025 | 15:20") ke format ISO 8601.
    4) *Pagination*: Kedua mode crawler mendukung crawling multi-halaman.

---

## ⚙️ Cara Menjalankan
1. Clone this repository:
   ```bash
   git clone https://github.com/[NAMA_ANDA]/bisnis-com-crawler.git
   cd bisnis-com-crawler

2. Create virtual environment and install dependencies:
    python -m venv venv
    # Activate
    venv\Scripts\activate  # (Windows)
    source venv/bin/activate  # (Mac/Linux)
    pip install -r requirements.txt

3. Jalankan Crawler:
    **Mode Standard (Berita Terbaru):**
        python crawl_standard.py
    **Mode Backtrack (Rentang Tanggal): (Opsional: Buka crawl_backtrack.py dan ubah start_date / end_date)**
        python crawl_backtrack.py

---

# 🧑‍💻 Author
**Deri Nugraha**
[LinkedIn](https://www.linkedin.com/in/deri-rizky-nugraha/) | [Github](https://github.com/xanjohn)

📧 deririzkynugraha0@gmail.com
