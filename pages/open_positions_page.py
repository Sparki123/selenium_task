from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List

from base.selenium import SeleniumBase


class OpenPositionsPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        driver.get("https://useinsider.com/careers/open-positions/?department=qualityassurance")
        self._filter_by_location: str = 'select2-filter-by-location-container'

    def get_filter_by_location(self) -> WebElement:
        return self.driver.find_element(By.ID, self._filter_by_location)

    def get_city(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//*[@id='select2-filter-by-location-result-q58v-Istanbul, Turkey']")

    def get_jobs(self) -> List[WebElement]:
        return self.driver.find_elements(By.XPATH, "//*[@id='jobs-list']/div")

    def get_apply_button(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//*[@id='jobs-list']/div[1]/div/a")
