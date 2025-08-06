from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from zoneinfo import ZoneInfo
import csv


def main():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    wait = WebDriverWait(driver, 10)
    driver.get("https://planetcinema.co.il")
    elem = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/section[3]/div/div/div/ul/li[2]/a")
        )
    )
    text = elem.text.strip()

    now = datetime.now(ZoneInfo("Asia/Jerusalem")).strftime("%Y-%m-%d %H:%M:%S")
    row = f"{now} - {text}"

    with open("output.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([row])

    driver.quit()


if __name__ == "__main__":
    main()
