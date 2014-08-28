"""
Test locator app forms
"""

import unittest
import datetime

from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AddTournamentFormSeleniumTest(LiveServerTestCase):
    """
    Add tournament form tests
    """
    def setUp(self):
        """
        Init webdriver instance
        """
        self.browser = webdriver.Firefox()


    def tearDown(self):
        """
        Close the browser
        """
        self.browser.quit()


    def test_add_form(self):
        """
        Add form tests with selenium
        Enter tournament data to add form and redirect
        to results form...test is add form redirects to results form
        """
        self.browser.get('http://localhost:8000/locator/add')

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Address', body.text)

        name = self.browser.find_element_by_name('name')
        name.send_keys('US Open')

        address = self.browser.find_element_by_name('address')
        address.send_keys('9500 Gilman Dr.')

        city = self.browser.find_element_by_name('city')
        city.send_keys('La Jolla')

        state = self.browser.find_element_by_name('state')
        state.send_keys('California')

        start_date = self.browser.find_element_by_name('start_date')
        start_date.send_keys(str(datetime.date.today()))

        end_date = self.browser.find_element_by_name('end_date')
        end_date.send_keys(
            str(datetime.date.today() + datetime.timedelta(days=5)))

        submit_button = self.browser.find_element_by_name('submit_button')
        submit_button.click()

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(
            'Your tournament has been added to the database', body.text)


class SearchTournamentFormSeleniumTest(LiveServerTestCase):
    """
    Add tournament form tests
    """
    def setUp(self):
        """
        Init webdriver instance
        """
        self.browser = webdriver.Firefox()


    def tearDown(self):
        """
        Close the browser
        """
        self.browser.quit()


    def test_add_form(self):
        """
        Add form tests with selenium
        Enter search query for tournament and redirect
        to search_results form...test is form redirects to search_results form
        """
        self.browser.get('http://localhost:8000/locator/search')

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Search for chess tournaments', body.text)

        state = self.browser.find_element_by_name('state')
        state.send_keys('California')

        search_button = self.browser.find_element_by_name('search_button')
        search_button.click()

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(
            'Chess tournament search results', body.text)