from django.http import HttpResponse
from django.shortcuts import render

# method view


def index(request):
    context = {
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
        ],
        'banner':'img/banner_home.png'
    }
    return render(request, 'index.html', context)
