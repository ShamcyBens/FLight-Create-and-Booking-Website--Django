from django.contrib import admin
from django.urls import path, include
from . import views
from .views import login_view

urlpatterns = [
    path('', views.register, name='register'),
    path('home/', views.home, name="home"),
    path('register/', views.register, name='register'),
    path('login/', login_view, name="login"),
    path('flights/create/', views.create_flight, name='create-flight'),
    path('flights/', views.flight_list, name='flight-list'),
    path('flights/<int:flight_id>/', views.flight_detail, name='flight-detail'),
    
]


