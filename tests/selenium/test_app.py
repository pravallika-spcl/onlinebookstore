from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

# Admin credentials
admin_username = "admin"  # Replace with actual admin username
admin_password = "admin"  # Replace with actual admin password

# Basic page title check
def basic_page_title_check():
    try:
        driver.get("http://localhost:8080/onlinebookstore/")  # Update with your home page URL
        time.sleep(3)  # Wait for page to load
        assert "Bookstore" in driver.title
        print("✅ Home Page Title Check Passed")
    except Exception as e:
        print(f"❌ Home Page Title Check Failed: {e}")
        exit(1)

# Admin login test
def login_as_admin():
    try:
        driver.get("http://localhost:8080/onlinebookstore/login")  # Update with your login URL
        time.sleep(2)  # Wait for the page to load

        # Enter admin credentials
        driver.find_element(By.ID, "username").send_keys(admin_username)  # Replace 'username' with actual ID if different
        driver.find_element(By.ID, "password").send_keys(admin_password)  # Replace 'password' with actual ID if different
        
        # Submit the login form
        driver.find_element(By.ID, "login-button").click()  # Replace 'login-button' with the actual login button ID
        
        time.sleep(3)  # Wait for the page to load after login
        
        # Check if login was successful
        if "Dashboard" in driver.title:  # Assuming Dashboard appears after login
            print("✅ Admin Login Successful!")
        else:
            print("❌ Admin Login Failed!")
