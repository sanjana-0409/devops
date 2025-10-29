import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setup_teardown():
    # Setup phase
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    # Teardown phase
    driver.quit()

def test_google_title(setup_teardown):
    driver = setup_teardown
    driver.get("https://www.google.com")
    assert "Google" in driver.title
