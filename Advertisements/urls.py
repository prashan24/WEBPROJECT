from django.urls import path
from . import views

urlpatterns = [
    path('',views.Advertisements, name='My Advertisements'),

]