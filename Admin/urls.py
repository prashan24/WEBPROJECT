from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_view, name='Admin'),
]