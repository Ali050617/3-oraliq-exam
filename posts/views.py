from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post, Category
from tags.models import Tag


def index(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    featured_posts = Post.objects.filter(featured=True)[:5]
    recent_posts = Post.objects.order_by('-created_at')[:5]

    context = {
        'categories': categories,
        'tags': tags,
        'featured_posts': featured_posts,
        'recent_posts': recent_posts,
    }
    return render(request, 'index_with_side_bar.html', context)


def post_list(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    category = request.GET.get('category')
    tag = request.GET.get('tag')
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    sort = request.GET.get('sort', '-created_at')

    if category:
        posts = posts.filter(category__slug=category)
    if tag:
        posts = posts.filter(tags__slug=tag)
    if date_from:
        posts = posts.filter(created_at__gte=date_from)
    if date_to:
        posts = posts.filter(created_at__lte=date_to)

    posts = posts.order_by(sort)

    ctx = {
        'posts': posts,
        'categories': categories,
        'tags': tags,
        'selected_category': category,
        'selected_tag': tag,
        'date_from': date_from,
        'date_to': date_to,
        'sort': sort,
    }
    return render(request, 'posts/post-detail.html', ctx)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'posts/post-detail.html', {'post': post})

