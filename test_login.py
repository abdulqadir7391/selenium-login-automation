from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def create_driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver

def test_valid_login():
    driver = create_driver()
    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

    expected_url = "https://practicetestautomation.com/logged-in-successfully/"
    if driver.current_url == expected_url:
        print("VALID LOGIN TEST PASSED ✔")
    else:
        print("VALID LOGIN TEST FAILED ❌", driver.current_url)

    driver.quit()

def test_invalid_login():
    driver = create_driver()
    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("WrongPassword")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

    error_message = driver.find_element(By.ID, "error").text
    if "Your password is invalid" in error_message:
        print("INVALID LOGIN TEST PASSED ✔")
    else:
        print("INVALID LOGIN TEST FAILED ❌", error_message)

    driver.quit()

if __name__ == "__main__":
    test_valid_login()
    test_invalid_login()
