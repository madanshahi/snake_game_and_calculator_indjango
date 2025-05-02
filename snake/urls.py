from django.urls import path
from . import views
urlpatterns=[
    path('',views.move_snake,name='snake'),
    path('end/',views.endGame, name='end')
]