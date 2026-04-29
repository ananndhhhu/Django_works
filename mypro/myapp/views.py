from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def first(request):
    return HttpResponse('First Page')

def second(request):
    return HttpResponse('Second Page')
