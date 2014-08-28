"""
URL Conf for locator app
"""

from django.conf.urls import patterns, url

from locator import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^add/$', views.add, name='add'),
    url(r'^results/$', views.results, name='results'),
    url(r'^search/$', views.search, name='search'),
    url(r'^search_results/$', views.search_results, name='search_results')
)

