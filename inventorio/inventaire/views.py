from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def liste(request):
    return render(request,
                  'liste/liste.html')
