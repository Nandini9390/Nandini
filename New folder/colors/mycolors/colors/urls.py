from django.urls import path
from . import views

urlpatterns = [
    path('red/', views.red, name='red'),
    path('pink/', views.pink, name='pink'),
    path('orange/',views.orange,name='orange'),
]