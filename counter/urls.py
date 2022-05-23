from django.urls import path
from . import views

app_name = 'counter'

urlpatterns = [
    path('', views.main, name='main'),
    path('counter/', views.week_number, name='counter'),
]