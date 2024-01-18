from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<str:blog_category>/', views.category, name='blog.category'),
    path('post/<slug:slugInput>/',views.singlePost, name='post.detail'),
]