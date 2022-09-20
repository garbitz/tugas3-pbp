# TODO: Implement Routings Here

from django.urls import path
from katalog.views import show_catalog
from mywatchlist.views import show_watchlist

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_watchlist, name='show_watchlist'),
]