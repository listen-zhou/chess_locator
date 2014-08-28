"""
Test Locator Views
"""

import sys

from django.test import TestCase
from django.core.urlresolvers import reverse, resolve

from locator.models import Tournaments
from locator.views import home, add, results, search, search_results


class URLResolverTests(TestCase):
    """
    Test if URL resolves to correct view
    """
    def test_home_resolve(self):
        """
        Test home page URL
        """
        found = resolve('/locator/')
        self.assertEqual(found.func, home)

    def test_add_resolve(self):
        """
        Test add tournament URL
        """
        found = resolve('/locator/add/')
        self.assertEqual(found.func, add)

    def test_results_resolve(self):
        """
        Test results of tournament add URL
        """
        found = resolve('/locator/results/')
        self.assertEqual(found.func, results)

    def test_search_resolve(self):
        """
        Test search page URL
        """
        found = resolve('/locator/search/')
        self.assertEqual(found.func, search)

    def test_search_results(self):
        """
        Test search results URL
        """
        found = resolve('/locator/search_results/')
        self.assertEqual(found.func, search_results)

class IndexViewTests(TestCase):
    """
    Test home view
    """
    def test_home(self):
        response = self.client.get(reverse('locator:home'))
        self.assertEqual(response.status_code, 200)


class AddViewTests(TestCase):
    """
    Test add tournament view
    """
    def test_add(self):
        response = self.client.get(reverse('locator:add'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)


class ResultsViewTests(TestCase):
    """
    Test results view
    """
    def test_results_w_valid_entry(self):
        """
        Get results page, check for status 200
        """
        tournament = Tournaments(
            name='Souther CA Open',
            address='500 Hotel Circle North',
            city='San Diego',
            state='CA',
            start_date='2014-09-01',
            end_date='2014-09-20'
        )
        tournament.save()
        url = '{}?id={}'.format(reverse('locator:results'), tournament.pk)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_retults_w_invalid_entry(self):
        """
        Get results page with invalid pk, check for 404
        """
        url = '{}?id={}'.format(reverse('locator:results'), sys.maxint)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

# class SearchResultsViewTests(TestCase):
#     def test_index(self):
#         response = self.client.get(reverse('locator:search_results'))
#         self.assertEqual(response.status_code, 200)