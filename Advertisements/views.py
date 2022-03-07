from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Advertisements(request):
    return render(request,'My_Ads.html')
