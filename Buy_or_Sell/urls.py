from django.urls import path
from . import views

urlpatterns = [
    path('', views.buy_or_sell, name='home'),
    path('contact/', views.contact, name='Contact'),
    path('dashboard/',views.dashboard, name='Dashboard'),
    path('buy/', views.buy, name='Buy'),
    path('sell/', views.sell, name='Sell'),
    path('find_offers/', views.find_offers, name='Find_Offers'),

]
