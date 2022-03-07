from django.shortcuts import render
# Create your views here.

def trade(request):
    return render(request, 'trade_requests.html')