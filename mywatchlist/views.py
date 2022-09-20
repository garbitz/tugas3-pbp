from django.shortcuts import render
from mywatchlist.models import WatchlistItem

# TODO: Create your views here.
def show_watchlist(request):
    data_watchlist = WatchlistItem.objects.all()
    context = {
        'list': data_watchlist,
        'nama': 'Muhammad Abizar Rachmanda',
        'id' : '2106751133',
    }
    return render(request, "mywatchlist.html", context)
