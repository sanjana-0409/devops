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

def test_addition(setup_teardown):
    driver = setup_teardown

    # Open the local HTML file (make sure path is correct)
    file_path = f"file:///{os.getcwd().replace('\\', '/')}/index.html"
    driver.get(file_path)

    # Enter numbers
    driver.find_element(By.ID, "num1").send_keys("5")
    driver.find_element(By.ID, "num2").send_keys("7")

    # Click add button
    driver.find_element(By.ID, "addButton").click()

    # Wait for result to update
    time.sleep(1)

    # Get result text
    result_text = driver.find_element(By.ID, "result").text

    # Assert the result is correct
    assert "Result: 12" == result_text, f"Expected 'Result: 12' but got '{result_text}'"
