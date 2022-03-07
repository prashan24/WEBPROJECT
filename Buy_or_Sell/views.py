from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def buy_or_sell(request):
    return render(request, 'buy_or_sell.html')

def dashboard(request):
    return  render(request, 'dashboard.html')

def buy(request):
    return render(request, 'buy_bitcoin.html')

def sell(request):
    return render(request, 'sell_ethereum.html')

def contact(request):
    return render(request, 'contact.html')

def find_offers(request):
    return  render(request, 'find_offers.html')


