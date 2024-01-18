from django.shortcuts import render

# Create your views here.

# import models
from .models import Post


def index(request):
    # queryset database table Post
    posts = Post.objects.all()
    context = {
        'title': 'Django Blog',
        'subtitle': 'Selamat Datang di halaman awal Blog',
        'category': 'Semua Kategori',
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
        ],
        'Posts': posts,
    }
    return render(request, 'blog/index.html', context)


def category(request, blog_category):
    # queryset database table Post
    posts = Post.objects.filter(category=blog_category)
    context = {
        'title': 'Django Blog',
        'subtitle': 'Filter Kategori '+blog_category,
        'category': 'Kategori '+blog_category,
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
        ],
        'Posts': posts,
    }
    return render(request, 'blog/index.html', context)


def singlePost(request, slugInput):
    post = Post.objects.get(slug=slugInput)
    context = {
        'title': post.title,
        'subtitle': 'Single Post ',
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
        ],
        'post': post,
    }
    return render(request, 'blog/singlePost.html', context)
