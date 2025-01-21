from django.shortcuts import render
from .models import Tag


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'index_with_side_bar.html', {'tags': tags})


def tag_detail(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    return render(request, 'index_with_side_bar.html', {'tag': tag})

