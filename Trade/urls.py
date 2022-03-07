from django.urls import path
from . import views

urlpatterns = [
    path('',views.trade, name='Trade Request'),

]