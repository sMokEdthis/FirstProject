"""
проверка что мы попали на страницу гелекси
1.открыть браузер*
2.перейти на страницу*
3. кликнуть по ссылке*
4. правильное содержание ссылки*

#1 окружение. Нужно указывать
# переменные которые мы будем использовать
from  selenium import webdriver
from selenium.webdriver.common.by import By
from pages.homepage import HomePage
from pages.product import ProductPage
import time
import pytest


#driver он же browser нужно оформить через фисктур
@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_open_s6(driver):

    driver.get('https://www.demoblaze.com/index.html')

    galaxy_s6 =driver.find_element(By.LINK_TEXT,'Samsung galaxy s6')

    galaxy_s6.click()

    title = driver.find_element(By.CSS_SELECTOR, 'h2')
    assert title.text == 'Samsung galaxy s6'

def test_two_monitors(driver):
    driver.get('https://www.demoblaze.com/index.html')

    monitor_link =driver.find_element(By.LINK_TEXT, 'Monitors')

    monitor_link.click()

    time.sleep(2)

    monitors = driver.find_elements(By.CSS_SELECTOR, '.col-lg-4.col-md-6.mb-4')

    assert len(monitors) == 2
"""