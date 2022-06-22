from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import wait

from base.selenium import SeleniumBase


class CareerPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        driver.get("https://useinsider.com/careers/")
        self.driver = driver
        self._location: str = 'career-our-location'
        self._teams: str = 'career-find-our-calling'
        self._life_at: str = '[data-id=a8e7b90]'
        self._all_teams: str = '//a[text()="See all teams"]'
        self._qa_department: str = '//h3[text()="Quality Assurance"]'
        self._see_all: str = '//a[text()="See all QA jobs"]'

    def get_location(self) -> WebElement:
        return self.is_visible("id", self._location, 'Location')

    def get_teams(self) -> WebElement:
        return self.is_visible("id", self._teams, 'Team')

    def get_life_in(self) -> WebElement:
        return self.is_visible("tag_name", self._life_at, 'Life at Insider')

    def get_all_teams(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//*[@id='career-find-our-calling']/div/div/a")

    def get_qa_department(self) -> WebElement:
        return self.is_visible("xpath", self._qa_department, 'QA department')

    def get_see_all_button(self) -> WebElement:
        return self.driver.get("xpath", self._see_all, 'See all button')
