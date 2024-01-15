from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'Django Blog',
        'subtitle': 'Selamat Datang di halaman awal Blog',
        'author': 'Mr Django',
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
        ],
        'banner': 'blog/img/banner_blog.png',
        'sub_link': [
            ['/blog', 'Django Blog'],
            ['/blog/cerita', 'Cerita'],
            ['/blog/news', 'News'],
        ],
    }
    return render(request, 'blog/index.html', context)


def news(request):
    context = {
        'title': 'News',
        'subtitle': 'Selamat Datang di halaman News',
        'author': 'News Papper',
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
        ],
        'banner': 'blog/img/banner_blog.png',
        'sub_link': [
            ['/blog', 'Django Blog'],
            ['/blog/cerita', 'Cerita'],
            ['/blog/news', 'News'],
        ],
    }
    return render(request, 'blog/index.html', context)


def cerita(request):
    context = {
        'title': 'Cerita',
        'subtitle': 'Selamat Datang di halaman Cerita',
        'author': 'Cerita Pagi',
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
        ],
        'banner': 'blog/img/banner_blog.png',
        'sub_link': [
            ['/blog', 'Django Blog'],
            ['/blog/cerita', 'Cerita'],
            ['/blog/news', 'News'],
        ],
    }
    return render(request, 'blog/index.html', context)
