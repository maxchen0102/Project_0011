

from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('home_view/', views.home_view, name='home_view'),
    path('data_text/', views.data_text, name='data_text'),
    path('some_view/', views.some_view, name='some_view'),
]
