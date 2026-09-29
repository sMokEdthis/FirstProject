from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import pytest
#driver он же browser нужно оформить через фисктур
@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()