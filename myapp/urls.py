

from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('test_view/', views.test_view, name='test_view'),
    path('data_test/', views.data_test, name='data_test'),
    path('some_view/', views.some_view, name='some_view'),
]
