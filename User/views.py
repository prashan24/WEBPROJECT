from django.shortcuts import render
from django.http import HttpResponse

def user_login(request):
    return render(request,'login_page.html')


    # Create your views here.
