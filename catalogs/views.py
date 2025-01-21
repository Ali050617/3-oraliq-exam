from django.shortcuts import render
from .models import Catalog


def catalog_list(request):
    catalogs = Catalog.objects.all()
    return render(request, 'index_with_side_bar.html', {'catalogs': catalogs})


def catalog_detail(request, catalog_id):
    catalog = Catalog.objects.get(id=catalog_id)
    return render(request, 'index_with_side_bar.html', {'catalog': catalog})

