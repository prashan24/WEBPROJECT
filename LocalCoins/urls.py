"""LocalCoins URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Buy_or_Sell
    2. Add a URL to urlpatterns:  path('', Buy_or_Sell.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.urls.conf import URLPattern

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Buy_or_Sell.urls')),
    path('', include('Login.urls')),
    path('', include('Register.urls')),
    path('User/', include('User.urls')),
    path('Advertisements/', include('Advertisements.urls')),
    path('Trade/', include('Trade.urls')),
    path('Wallets/', include('Wallets.urls')),
    path('Transactions/', include('Transactions.urls')),
    path('Support/', include('Support.urls')),
    path('Admin/', include('Admin.urls')),
]
