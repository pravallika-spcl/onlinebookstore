from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

# Update with actual admin credentials
admin_username = "admin"  # Replace with actual admin username
admin_password = "adminpassword"  # Replace with actual admin password

def login_as_admin():
    try:
        driver.get("http://localhost:8080/onlinebookstore/SellerLogin.html")  # Update with your login URL
        time.sleep(2)  # Wait for the page to load

        # Enter admin credentials
        driver.find_element(By.ID, "username").send_keys(admin_username)  # Replace 'username' with actual ID if different
        driver.find_element(By.ID, "password").send_keys(admin_password)  # Replace 'password' with actual ID if different
        
        # Click the login button using class name
        driver.find_element(By.CLASS_NAME, "AdminLogin").click()  # Using class 'AdminLogin' to find the login button
        
        time.sleep(3)  # Wait for the page to load after login
        
        # Check if login was successful (You can change the success condition based on your app)
        if "Dashboard" in driver.title:  # Assuming Dashboard appears after login
            print("✅ Admin Login Successful!")
        else:
            print("❌ Admin Login Failed!")
            exit(1)
    
    except Exception as e:
        print(f"❌ Test Failed: {e}")
        exit(1)

# Run the login test
login_as_admin()

# Optionally, you can add further tests here for other pages after login.

# Close the browser
driver.quit()
