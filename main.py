from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="/home/spravallika/Desktop/Selenium/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("http://10.201.0.3:8080/onlinebookstore/")

driver.find_element(By.XPATH, '//a[@href="CustomerLogin.html"]').click()
time.sleep(1)

driver.find_element(By.XPATH, '//a[@href="SellerLogin.html"]').click()
time.sleep(1)

driver.find_element(By.ID, "userName").send_keys("admin")
time.sleep(1)

driver.find_element(By.ID, "Password").send_keys("admin")
time.sleep(1)

driver.find_element(By.CLASS_NAME, "AdminLogin").click()
time.sleep(1)

time.sleep(5)