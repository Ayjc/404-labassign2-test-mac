from django.shortcuts import render
from django.http import HttpResponse # Make sure to include this import


# Create your views here.
def index(request):
    return render(request, "index.html")