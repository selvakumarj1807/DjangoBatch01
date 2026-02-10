from django.urls import  path

from app03 import views

urlpatterns = [
    path('', views.app03_index),
    
]
