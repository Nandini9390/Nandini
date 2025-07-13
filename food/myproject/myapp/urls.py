from django.urls import path
from . import views

urlpatterns = [
    path('', views.Bakerys_list, name='Bakerys_list'),
    path('Bakerys/<int:pk>/', views.Bakerys_detail, name='Bakerys_detail'),
]


urlpatterns = [
    path('', views.canteen_list, name='canteen_list'),
    path('canteen/<int:pk>/', views.canteen_detail, name='canteen_detail'),

]



urlpatterns = [
    path('', views.mess_list, name='mess_list'),
    path('mess/<int:pk>/', views.mess_detail, name='mess_detail'),
]