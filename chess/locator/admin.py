"""
Admin resistration for locator app
"""

from django.contrib import admin

from locator.models import Tournaments


class TournamentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'city', 'state', 'start_date', 'end_date')

admin.site.register(Tournaments, TournamentsAdmin)