from platform import release
from pyexpat import model
from django.db import models

class WatchlistItem(models.Model):
    # watched = models.TextField()
    # title = models.TextField()
    # rating = models.IntegerField()
    # release_date = models.TextField()
    # review = models.TextField()
    item_name = models.CharField(max_length=255)
    item_price = models.BigIntegerField()
    item_stock = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField()
    item_url = models.URLField()