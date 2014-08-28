"""
Models for locator app
"""

from django.db import models

class Tournaments(models.Model):
    """
    Model used to store tournament data
    """
    STATES = (
        ('CA', 'California'),
        ('NV', 'Nevada'),
        ('NY', 'New York'),
    )
    name = models.CharField(max_length=40, blank=False)
    link = models.URLField(max_length=200, blank=True)
    address = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=25, blank=False)
    state = models.CharField(
        max_length=2, choices=STATES, blank=False, default='CA')
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)

    def __unicode__(self):
        return self.name




