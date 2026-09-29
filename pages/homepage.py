from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.demoblaze.com/index.html')

    def click_galaxy_s6(self):
        galaxy_s6 = self.driver.find_element(By.LINK_TEXT, 'Samsung galaxy s6')
        galaxy_s6.click()

    def click_monitor(self):
        monitor = self.driver.find_element(By.LINK_TEXT, 'Monitors')
        monitor.click()

    def check_products_count(self, count):
        monitors = self.driver.find_elements(By.CSS_SELECTOR, '.col-lg-4.col-md-6.mb-4')
        assert len(monitors) == count

