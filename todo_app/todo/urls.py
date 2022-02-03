from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('delete/<int:pk>', views.delete,name='delete'),
]