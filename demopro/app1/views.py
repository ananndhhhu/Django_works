from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('Welcome To Django')

def index(request):
    return HttpResponse('Hallo')
