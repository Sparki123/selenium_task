from selenium.webdriver.remote.webelement import WebElement

from base.selenium import SeleniumBase


class MainPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._menu_more: str = '//span[text()="More"]'
        self._careers_link: str = '//h5[text()="Careers"]'

    def get_menu_more_tab(self) -> WebElement:
        return self.is_visible("xpath", self._menu_more, 'Menu More')

    def get_careers(self) -> WebElement:
        return self.is_visible("xpath", self._careers_link, 'Career Link')
