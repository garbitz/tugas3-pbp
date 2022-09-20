from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    data_katalog = CatalogItem.objects.all()
    context = {
        'list': data_katalog,
        'nama': 'Muhammad Abizar Rachmanda',
        'id' : '2106751133',
    }
    return render(request, "katalog.html", context)
