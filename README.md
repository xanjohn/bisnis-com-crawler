# 📰 Crawler & Scraper Berita Bisnis.com

> “Sebuah pipeline data engineering end-to-end yang dibuat untuk melakukan crawl dan scrape artikel berita dari portal bisnis.com”

---

## 🧩 Project Overview
Proyek ini adalah crawler dan scraper Python yang dirancang untuk mengambil artikel berita dari bisnis.com menggunakan library Beautifulsoup4

Arsitektur proyek ini bersifat modular, memisahkan logika inti Scraper (yang mengambil detail satu artikel) dari Crawler (yang menemukan link artikel). Proyek ini memiliki dua mode eksekusi (entrypoint) yang berbeda sesuai kebutuhan.


## ⚙️ Project Overview
1. Standard Mode (crawl_standard.py):

2. Backtrack Mode (crawl_backtrack.py):



Berperan sebagai crawler yang dapat dijadwalkan secara berkala untuk mengambil artikel terbaru.

Memulai crawling dari halaman indeks utama (https://www.bisnis.com/index).

Secara otomatis menangani paginasi (halaman ganda) untuk menemukan semua artikel terbaru.

Menyimpan hasilnya sebagai hasil_scraping_standard.json.




**Workflow:**
1. Data scraping  
2. Case Folding, Text cleaning and normalization
4. Feature extraction (TF-IDF)
5. Split Data (80:20)
6. Model training and evaluation (SVM)

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

## 🧮 Modeling Summary

*Validation Data
| Dimension | Model | Precision | Recall | F1-Score | Accuracy | 
|------------|--------|------------|--------|-----------|-----------|
| I/E | SVM | 0.697 | 0.679 | 0.591 | 0.679 |
| J/P | SVM | 0.658 | 0.645 | 0.614 | 0.602 |
| N/S | SVM | 0.625 | 0.602 | 0.581 | 0.690 |
| T/F | SVM | 0.710 | 0.690 | 0.625 | 0.645 |

*Test Data
| Dimension | Model | Precision | Recall | F1-Score | Accuracy | 
|------------|--------|------------|--------|-----------|-----------|
| I/E | SVM | 0.560 | 0.658 | 0.558 | 0.658 |
| J/P | SVM | 0.565 | 0.546 | 0.510 | 0.561 |
| N/S | SVM | 0.538 | 0.561 | 0.537 | 0.595 |
| T/F | SVM | 0.533 | 0.595 | 0.502 | 0.546 |

---

## 🧰 Tech Stack
- **Python** (Pandas, NumPy, Scikit-learn, NLTK, TQDM)
- **Visualization:** Matplotlib, Seaborn
- **NLP:** Text preprocessing, tokenization, normalization
- **Augmentation:** Back Translation, Synonym Replacement
- **Modeling:** Support Vector Machine (SVM)
- **Evaluation:** F1-score, Precision, Recall, Confusion Matrix

---

## ⚙️ How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/xanjohn/MBTI-indonesian-tweet-classification.git
   cd mbti-nlp-classification

2. Create virtual environment and install dependencies:
    python -m venv venv
    # Activate
    venv\Scripts\activate  # (Windows)
    source venv/bin/activate  # (Mac/Linux)
    pip install -r requirements.txt

3. Open the notebooks in Jupyter and run them sequentially:
    Jupyter Notebook


# 📈 Results
    - The accuracy for test data and validation data it's bad
    - It's using full praprocess


# 📂 Results Preview
See the results/figures/ folder for:
    - Precission
    - Recall
    - F1-score
    - Accuracy

# 🧑‍💻 Author
**Deri Nugraha**
[LinkedIn](https://www.linkedin.com/in/deri-rizky-nugraha/) | [Github](https://github.com/xanjohn)

📧 deririzkynugraha0@gmail.com
