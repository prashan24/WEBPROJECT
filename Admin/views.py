from django.shortcuts import render

# Create your views here.

def admin_view(request):
    return render(request, 'admin_view.html')