from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait

from base.selenium import SeleniumBase
from selenium.webdriver.common.action_chains import ActionChains


class CareerPage(SeleniumBase):
    def __init__(self, driver, url=None):
        super().__init__(driver)
        if url is not None:
            driver.get(url)
        self.driver = driver
        self._location: str = 'career-our-location'
        self._teams: str = 'career-find-our-calling'
        self._life_at: str = '[data-id=a8e7b90]'
        self._all_jobs: str = '//a[contains(text(),"See all QA jobs")]'
        self._qa_department: str = '//div[12]/div[1]/a[1]'
        self._see_all: str = '//a[contains(text(),"See all teams")]'

    def get_location(self) -> WebElement:
        return self.is_visible("id", self._location, 'Location')

    def get_teams(self) -> WebElement:
        return self.is_visible("id", self._teams, 'Team')

    def get_life_in(self) -> WebElement:
        return self.is_visible("tag_name", self._life_at, 'Life at Insider')

    def get_qa_department(self) -> WebElement:
        return self.driver.find_element(By.XPATH, self._qa_department)

    def get_see_all_button(self) -> WebElement:
        return self.driver.find_element(By.XPATH, self._see_all)

    def get_all_jobs(self) -> WebElement:
        return self.driver.find_element(By.XPATH, self._all_jobs)

