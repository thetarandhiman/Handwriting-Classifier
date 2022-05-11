from unicodedata import name
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='index'),
    path("index", views.index, name='index'),
    path("options", views.options, name='options'),
    path("training", views.training, name='training'),
    path("training2", views.training2, name='training2'),
    path("testing", views.testing, name='testing'),
]