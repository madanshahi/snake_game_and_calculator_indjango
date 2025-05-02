from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='contact'),         # root path
    path('mysite/', views.mysite, name='welcome'),         # no leading slash and correct name
]
