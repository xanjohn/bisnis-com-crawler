import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime

# Kamus untuk menerjemahkan bulan
month_map = {
    "Januari": 1, "Februari": 2, "Maret": 3, "April": 4, "Mei": 5, "Juni": 6,
    "Juli": 7, "Agustus": 8, "September": 9, "Oktober": 10, "November": 11, "Desember": 12
}

def scrape_article_details(url):
    print(f"--- Scraping detail dari: {url} ---")
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error: Gagal mengakses {url}")
            return None
        soup = BeautifulSoup(response.content, 'html.parser') #Inisiasi
        # 1. Judul
        title_tag = soup.find("h1", class_="detailsTitleCaption")
        title_text = title_tag.get_text(strip=True) if title_tag else "Judul Tidak Ditemukan"
        
        # 2. Tanggal
        date_tag = soup.find("div", class_="detailsAttributeDates")
        date_text_raw = date_tag.get_text(strip=True) if date_tag else ""
        iso_date = date_text_raw # Default jika gagal
        
        #Konversi Tanggal Menjadi format ISO 8601
        if date_text_raw:
            try:
                # date_text_raw = "Jumat, 14 November 2025 | 15:20"
                parts = date_text_raw.split(' | ')
                date_part = parts[0] # "Jumat, 14 November 2025"
                time_part = parts[1] # "15:20"
                clean_date_part = date_part.split(', ')[1] # "14 November 2025"
                day_str, month_str, year_str = clean_date_part.split(' ')
                month_int = month_map.get(month_str)
                hour_str, minute_str = time_part.split(':')
                
                if month_int:
                    dt = datetime(
                        year=int(year_str),
                        month=month_int,
                        day=int(day_str),
                        hour=int(hour_str),
                        minute=int(minute_str)
                    )
                    iso_date = dt.isoformat()
            
            except Exception as e:
                print(f"Parsing tanggal gagal: {e}. Menyimpan nilai mentah: {date_text_raw}")
                iso_date = date_text_raw

        # 3. Isi Artikel
        article_body = soup.find("article", class_="detailsContent")
        isi_artikel_text = "Isi Artikel Tidak Ditemukan"
        if article_body:
            paragraphs = article_body.select("p:not(.disclaimer)")
            text_list = []
            for p in paragraphs:
                if "Baca Juga" not in p.get_text():
                    text_list.append(p.get_text(strip=True))
            isi_artikel_text = " ".join(text_list)
            
        # 4. Output Dictionary
        output_data = {
            "link": url,
            "judul": title_text,
            "tanggal_terbit": iso_date,
            "isi_artikel": isi_artikel_text
        }
        return output_data

    except Exception as e:
        print(f"Gagal scrape {url}: {e}")
        return None