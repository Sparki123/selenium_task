import pytest

from pages.main_page import MainPage
from pages.career_page import CareerPage
from pages.open_positions_page import OpenPositionsPage


@pytest.mark.usefixtures('setup')
class Tests:
    def test_nav_links(self):
        main_page = MainPage(self.driver)
        more_tab = main_page.get_menu_more_tab()

        assert more_tab
        more_tab.click()
        main_page.get_careers().click()

        career_page = CareerPage(self.driver)

        assert career_page.get_teams()
        assert career_page.get_location()
        assert career_page.get_life_in()

        career_page.get_see_all_button().click()
        career_page.get_qa_department().click()
        career_page.get_see_all_button().click()

        open_position = OpenPositionsPage(self.driver)
        open_position.get_filter_by_location()

    def test_career_page(self):
        career_page = CareerPage(self.driver)

        assert career_page.get_teams()
        assert career_page.get_location()
        assert career_page.get_life_in()

        career_page.get_see_all_button().click()  #here i had problem, cant click on element, but im tryed
        career_page.get_qa_department().click()
        career_page.get_see_all_button().click()

        open_position = OpenPositionsPage(self.driver)
        open_position.get_filter_by_location()
        assert open_position.get_filter_by_location()

    def test_open_positions(self):
        open_positions_page = OpenPositionsPage(self.driver)

        open_positions_page.get_filter_by_location().click()
        open_positions_page.get_city().click()  #here i had problem, cant click on element, but im tryed
        jobs = open_positions_page.get_jobs()

        assert jobs

        open_positions_page.get_apply_button().click()

        assert "https://jobs.lever.co/" in self.driver.current_url


