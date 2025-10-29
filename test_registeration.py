import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

@pytest.fixture
def setup_teardown():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_registration(setup_teardown):
    driver = setup_teardown

    # Open your local HTML file
    file_path = f"file:///{os.getcwd().replace('\\', '/')}/register.html"  # or register.html
    driver.get(file_path)

    # Fill the form fields
    driver.find_element(By.ID, "name").send_keys("Sanjana Patnaikuni")
    driver.find_element(By.ID, "email").send_keys("sanjana@example.com")
    driver.find_element(By.ID, "password").send_keys("secure123")

    # Click Register
    driver.find_element(By.ID, "registerBtn").click()

    # Wait for the message to appear
    time.sleep(1)

    # Verify message text
    message = driver.find_element(By.ID, "message").text
    assert message == "Registration successful!", f"Expected success message, got: '{message}'"
