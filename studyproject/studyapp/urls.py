from .import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    #path('add/', views.arithmetic_operations,name='addition'),
    #path('sub/', views.substraction, name='substraction'),
    #path('divi/', views.division, name='division'),
    #path('mul/', views.multiplication, name='multiplication'),
]