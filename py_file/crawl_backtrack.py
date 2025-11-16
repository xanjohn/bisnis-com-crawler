import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime, timedelta

#import module
from scraper import scrape_article_details

#Inisiasi Entrypoint
start_date = datetime(2025, 11, 15)
end_date = datetime(2025, 11, 16)

date_list = []
current_date = start_date
while current_date <= end_date:
    date_list.append(current_date)
    current_date += timedelta(days=1)
print(f"Akan men-crawl {len(date_list)} hari...")

all_links_to_scrape = []
base_url = "https://bisnis.com/"


for date in date_list:
    # Format tanggal yang benar (YYYY-MM-DD)
    date_str = date.strftime("%Y-%m-%d")
    
    # link entrypoint
    indeks_url_page_1 = f"https://www.bisnis.com/index?categoryId=0&type=indeks&date={date_str}&type=indeks"
    
    current_page_url = indeks_url_page_1
    page_num = 1
    
    
    while current_page_url:
        print(f"--- Mengambil link dari Tgl: {date_str}, Halaman: {page_num} ---")
        print(f"URL: {current_page_url}")
        
        try:
            response = requests.get(current_page_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # 1. Scrap semua berita pada halaman
            links_found_on_this_page = 0
            for title_tag in soup.find_all(["h2", "h4"], class_="artTitle"):
                parent_a_tag = title_tag.find_parent("a")
                if parent_a_tag and parent_a_tag.get('href'):
                    href = parent_a_tag['href']
                    full_url = urljoin(base_url, href)
                    if full_url not in all_links_to_scrape:
                        all_links_to_scrape.append(full_url)
                        links_found_on_this_page += 1
            print(f"Ditemukan {links_found_on_this_page} link baru.")

            # 2. Pagination
            next_button = soup.find("a", rel="next") 
            
            if next_button and next_button.get('href'):
                current_page_url = urljoin(base_url, next_button['href'])
                page_num += 1
            else:
                print(f"Halaman 'Next' tidak ditemukan untuk Tgl: {date_str}. Selesai.")
                current_page_url = None

        except Exception as e:
            print(f"Gagal memproses halaman {current_page_url}: {e}")
            current_page_url = None

print(f"\nTotal {len(all_links_to_scrape)} link artikel unik ditemukan dari semua tanggal dan halaman.")
print("\n--- MULAI PROSES SCRAPING DETAIL ARTIKEL ---")
all_articles_data = []

for link in all_links_to_scrape:
    article_data = scrape_article_details(link)
    
    if article_data and article_data["judul"] != "Judul Tidak Ditemukan":
        all_articles_data.append(article_data)
    else:
        print(f"SKIPPING (Artikel premium atau error): {link}")

output_filename = f"backtrack_{start_date.strftime('%Y%m%d')}_{end_date.strftime('%Y%m%d')}.json"
print(f"\n--- Scraping Selesai ---")
print(f"Total {len(all_articles_data)} artikel berhasil diambil.")

#Simpan JSON
try:
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(all_articles_data, f, indent=4, ensure_ascii=False)
    
    print(f"Sukses menyimpan data ke {output_filename}")
except Exception as e:
    print(f"ERROR: Gagal menyimpan file JSON. {e}")
print("Selesai.")
