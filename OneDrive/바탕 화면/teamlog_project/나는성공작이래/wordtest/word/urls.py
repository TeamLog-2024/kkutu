from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('main/',views.main, name="main"),
    path('crawling/', views.crawling, name="crawling"),
    path('word/', views.word, name="word"),
    path('test/', views.test, name="test"),
]
