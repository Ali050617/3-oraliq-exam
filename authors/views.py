from django.shortcuts import render
from .models import Author


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'index_with_side_bar.html', {'authors': authors})


def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, 'index_with_side_bar.html', {'authors': author})

