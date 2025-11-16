import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin

#Import Module
from scraper import scrape_article_details

base_url = "https://bisnis.com/"

all_links_to_scrape = []

current_page_url = "https://www.bisnis.com/index" 
page_num = 1


while current_page_url and page_num <= 2:
# while current_page_url:
    print(f"--- Mengambil daftar link dari Halaman Indeks ke-{page_num} ---")
    print(f"URL: {current_page_url}")
    
    try:
        response = requests.get(current_page_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 1. Ambil semua link artikel di halaman ini
        links_found_on_this_page = 0
        for title_tag in soup.find_all(["h2", "h4"], class_="artTitle"):
            parent_a_tag = title_tag.find_parent("a")
            if parent_a_tag and parent_a_tag.get('href'):
                href = parent_a_tag['href']
                full_url = urljoin(base_url, href)
                if full_url not in all_links_to_scrape:
                    all_links_to_scrape.append(full_url)
                    links_found_on_this_page += 1
        
        print(f"Ditemukan {links_found_on_this_page} link baru di halaman ini.")

        # 2.Pagination
        next_button = soup.find("a", rel="next") 
        if next_button and next_button.get('href'):
            current_page_url = urljoin(base_url, next_button['href'])
            page_num += 1
        else:
            print("Tombol 'Next' (rel='next') tidak ditemukan. Selesai crawling link.")
            current_page_url = None

    except Exception as e:
        print(f"Gagal memproses halaman {current_page_url}: {e}")
        current_page_url = None

print(f"\nTotal {len(all_links_to_scrape)} link artikel unik ditemukan dari semua halaman.")
print("\n--- MULAI PROSES SCRAPING DETAIL ARTIKEL ---")
all_articles_data = []

for link in all_links_to_scrape:
    article_data = scrape_article_details(link)
    
    if article_data and article_data["judul"] != "Judul Tidak Ditemukan":
        all_articles_data.append(article_data)
    else:
        print(f"SKIPPING (Artikel premium atau error): {link}")

output_filename = 'hasil_scraping_standard.json'
print(f"\n--- Scraping Selesai ---")
print(f"Total {len(all_articles_data)} artikel berhasil diambil.")
print(f"Menyimpan data ke {output_filename}...")

#Simpan JSON
with open(output_filename, 'w', encoding='utf-8') as f:
    json.dump(all_articles_data, f, indent=4, ensure_ascii=False)

print("Selesai.")