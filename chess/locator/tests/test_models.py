"""
Test locator app models
"""

import unittest

import mock

from locator.models import Tournaments

class TournamentModelTests(unittest.TestCase):
    """
    Test Tournament Model
    """
    def test_poll_objects_are_named_after_their_question(self):
        """
        Test unicode for Tournaments instance
        """
        mock_tournament = mock.Mock(spec=Tournaments)
        mock_tournament.name = 'So Cal Open'
        self.assertEquals(
            Tournaments.__unicode__(mock_tournament), 'So Cal Open')
