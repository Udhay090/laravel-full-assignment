from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.binary_location = "/snap/bin/chromium"
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--user-data-dir=/tmp/chrome-selenium-profile")

driver = webdriver.Chrome(options=options)
driver.get("http://da.adlynk.in:8000/login")

email_field = driver.find_element(By.NAME, "email_address")
password_field = driver.find_element(By.NAME, "password")

email_field.send_keys("test@example.com")
password_field.send_keys("randompass123")

login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
login_button.click()

time.sleep(2)
driver.quit()
print("Login form submitted successfully")
