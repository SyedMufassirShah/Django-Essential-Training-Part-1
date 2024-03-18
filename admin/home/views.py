from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return HttpResponse("Hello Ladies")

# url -> localhost:8000/home_template
def home(request):
    return render(request,'home/home.html',{})

@login_required(login_url='/admin/')
def authorized(request):
    return render(request,'home/authorized.html', {})

