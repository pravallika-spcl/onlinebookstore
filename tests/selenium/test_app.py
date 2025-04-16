from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    driver.get("http://localhost:8080/onlinebookstore/")
    time.sleep(3)  # wait for page to load
    assert "Online Bookstore" in driver.title
    print("✅ Test Passed: Title matched")
except Exception as e:
    print(f"❌ Test Failed: {e}")
    exit(1)
finally:
    driver.quit()

