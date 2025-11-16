# 📰 Crawler & Scraper Berita Bisnis.com

> “Sebuah pipeline data engineering end-to-end yang dibuat untuk melakukan crawl dan scrape artikel berita dari portal bisnis.com”

---

## 🧩 Project Overview
Proyek ini adalah crawler dan scraper Python yang dirancang untuk mengambil artikel berita dari bisnis.com menggunakan library Beautifulsoup4

Arsitektur proyek ini bersifat modular, memisahkan logika inti Scraper (yang mengambil detail satu artikel) dari Crawler (yang menemukan link artikel). Proyek ini memiliki dua mode eksekusi (entrypoint) yang berbeda sesuai kebutuhan.


## ⚙️ Penjelasan Program
1. Standard Mode (crawl_standard.py):
    1) Berperan sebagai crawler yang dapat dijadwalkan secara berkala untuk mengambil artikel terbaru.
    2) Memulai crawling dari halaman indeks utama (https://www.bisnis.com/index).
    3) Secara otomatis menangani paginasi (halaman ganda) untuk menemukan semua artikel terbaru.
    4) Menyimpan hasilnya sebagai hasil_scraping_standard.json.

2. Backtrack Mode (crawl_backtrack.py):
    1) Menerima parameter start_date dan end_date (saat ini di-hardcode di dalam skrip).
    2) Melakukan looping untuk setiap tanggal dalam rentang tersebut.
    3) Mengunjungi halaman indeks spesifik per tanggal (misal: .../index?date=YYYY-MM-DD).
    4) Menangani paginasi di setiap halaman indeks tanggal untuk memastikan semua artikel terambil.
    5) Menyimpan hasilnya sebagai file JSON dinamis, misal backtrack_20251115_20251116.json.

---

## 🧰 Teknologi yang dipakai
- **Python**
- **Library yang dipakai:**:
    * *Requests*: Untuk mengirim permintaan HTTP ke bisnis.com.
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
    ```bash
    python -m venv venv
    # Activate
    venv\Scripts\activate  # (Windows)
    source venv/bin/activate  # (Mac/Linux)
    pip install -r requirements.txt

3. Jalankan Crawler:
    **Mode Standard (Berita Terbaru):**
    ```bash
        python crawl_standard.py
    ```

    **Mode Backtrack (Rentang Tanggal): (Opsional: Buka crawl_backtrack.py dan ubah start_date / end_date)**
    ```bash
        python crawl_backtrack.py
    ```

---

# 🧑‍💻 Author
**Deri Nugraha**
[LinkedIn](https://www.linkedin.com/in/deri-rizky-nugraha/) | [Github](https://github.com/xanjohn)

📧 deririzkynugraha0@gmail.com
