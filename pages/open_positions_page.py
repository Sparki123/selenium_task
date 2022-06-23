from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List

from base.selenium import SeleniumBase


class OpenPositionsPage(SeleniumBase):
    def __init__(self, driver, url = None):
        super().__init__(driver)
        if url is not None:
            driver.get(url)
        self.driver = driver
        self._filter_by_location: str = 'select2-filter-by-location-container'
        self._city: str = '//span[2]/ul[1]/li[13]'

    def get_filter_by_location(self) -> WebElement:
        return self.driver.find_element(By.ID, self._filter_by_location)

    def get_city(self) -> WebElement:
        return self.driver.find_element(By.XPATH, self._city)

    def get_jobs(self) -> List[WebElement]:
        return self.driver.find_elements(By.XPATH, "//*[@id='jobs-list']/div")

    def get_apply_button(self) -> WebElement:
        return self.driver.find_elements(By.XPATH, "//a[text()='Apply Now']")[0]

