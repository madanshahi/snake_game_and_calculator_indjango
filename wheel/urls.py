# wheel/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.spin_page, name='spin_page'),
    path('spin/', views.spin_wheel, name='spin_wheel'),
]
