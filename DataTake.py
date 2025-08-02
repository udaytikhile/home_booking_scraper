from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import os

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

file = 0
os.makedirs("data", exist_ok=True)

url = "https://www.booking.com/searchresults.en-gb.html?ss=Mumbai&checkin=2025-08-15&checkout=2025-08-16&group_adults=2&no_rooms=1&group_children=0"
driver.get(url)
time.sleep(5)

for page in range(1, 21):
    print(f"\nScraping Page {page}")
    time.sleep(3)

    # Find hotel cards
    products = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')
    print(f"Found {len(products)} listings")

    for product in products:
        html = product.get_attribute("outerHTML")
        with open(f"data/hotel_{file}.html", "w", encoding="utf-8") as f:
            f.write(html)
        file += 1

    # Try clicking the next button
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, 'button[type="button"]')
        driver.execute_script("arguments[0].scrollIntoView();", next_button)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", next_button)
    except NoSuchElementException:
        print("Next button not found. Ending.")
        break

driver.quit()
