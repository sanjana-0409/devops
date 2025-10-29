import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setup_teardown():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_google_search_button_exists(setup_teardown):
    driver = setup_teardown
    driver.get("https://www.google.com")

    # Accept cookies or privacy consent if shown
    try:
        consent_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button/div[contains(text(),'Accept all') or contains(text(),'I agree')]"))
        )
        consent_button.click()
    except Exception:
        pass  # Skip if not shown

    # Type something to make the search button visible
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("Selenium")
    
    # Wait until the search button is clickable
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "btnK"))
    )

    # Assert that it is visible
    assert search_button.is_displayed(), "Google Search button not found or not visible on the page"
