import pytest

from pages.main_page import MainPage
from pages.career_page import CareerPage
from pages.open_positions_page import OpenPositionsPage


@pytest.mark.usefixtures('setup')
class Tests:
    def test_nav_links(self):
        # # Visit https://useinsider.com/ and check Insider home page is opened or not
        main_page = MainPage(self.driver)
        more_tab = main_page.get_menu_more_tab()

        assert more_tab

        # Select “More” menu in navigation bar, select “Careers” and check Career page, its
        # Locations, Teams and Life at Insider blocks are opened or not
        more_tab.click()
        main_page.get_careers().click()
        career_page = CareerPage(self.driver)

        assert career_page.get_teams()
        assert career_page.get_location()
        assert career_page.get_life_in()

    def test_career_page(self):
        #  Click “See All Teams”, select Quality Assurance, click “See all QA jobs”, filter jobs by
        # Location - Istanbul, Turkey and department - Quality Assurance, check presence of
        # jobs list
        career_page = CareerPage(self.driver, "https://useinsider.com/careers/")

        try:
            career_page.get_see_all_button().click()
        except BaseException:
            print("I dont know how fix it")

        career_page.get_see_all_button().click()

        try:
            career_page.get_qa_department().click()
        except BaseException:
            print("I dont know how fix it, i used move to element, ActionChains, but it doesn helped me")

        career_page.get_qa_department().click()
        career_page.get_all_jobs().click()

        open_position = OpenPositionsPage(self.driver)
        open_position.get_filter_by_location()
        assert open_position.get_filter_by_location()

    def test_open_positions(self):
        #  Check that all jobs’ Position contains “Quality Assurance”, Department contains
        # “Quality Assurance”, Location contains “Istanbul, Turkey” and “Apply Now” button
        #  Click “Apply Now” button and check that this action redirects us to Lever Application
        # form page
        open_positions_page = OpenPositionsPage(self.driver, "https://useinsider.com/careers/open-positions"
                                                             "/?department=qualityassurance")

        open_positions_page.get_filter_by_location().click()
        open_positions_page.get_city().click()
        jobs = open_positions_page.get_jobs()

        assert jobs

        open_positions_page.get_apply_button().click()

        assert "https://jobs.lever.co/" in self.driver.current_url


