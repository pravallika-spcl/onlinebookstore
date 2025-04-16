from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import traceback

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

try:
    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:8080/onlinebookstore/")
    time.sleep(3)  # wait for page to load
    print(f"Page title: {driver.title}")
    assert "Online Bookstore" in driver.title
    print("✅ Test Passed: Title matched")
except Exception as e:
    print(f"❌ Test Failed: {e}")
    traceback.print_exc()
    exit(1)
finally:
    try:
        driver.quit()
    except:
        pass
