import time
from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

app = Flask(__name__)

def fetch_student_data(npm):
    url = f"https://pddikti.kemdiktisaintek.go.id/search/{npm}"
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.178 Safari/537.36")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)

        # Tunggu hingga elemen utama termuat (maksimal 10 detik)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "detail-data"))
        )

        time.sleep(2)  # Tambahan waktu agar halaman stabil
        html = driver.page_source

        # Debugging: Simpan HTML yang didapat
        with open("debug.html", "w", encoding="utf-8") as f:
            f.write(html)

    except Exception as e:
        print("Error saat mengakses halaman:", e)
        html = None
    finally:
        driver.quit()
    
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        biodata = {}

        detail_div = soup.find("div", id="detail-data")
        if detail_div:
            paragraphs = detail_div.find_all("p")
            for p in paragraphs:
                text = p.get_text(strip=True)
                if ':' in text:
                    key, value = text.split(":", 1)
                    biodata[key.strip()] = value.strip()
            return biodata
    return None

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        npm = request.form.get("npm")
        if npm:
            result = fetch_student_data(npm)
            if not result:
                error = "Data tidak ditemukan atau terjadi kesalahan saat mengambil data."
        else:
            error = "Masukkan NPM yang valid."
    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
