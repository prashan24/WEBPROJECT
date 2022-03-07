from django.shortcuts import render

# Create your views here.

def wallets(request):
    return  render(request, 'wallets.html')