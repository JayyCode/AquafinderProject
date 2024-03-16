from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def divesearch (resquest):
    return HttpResponse("Search Engine")

def index(request):
    return HttpResponse("Welcome Home Nigga")

def discovery(request):
    return HttpResponse("you found a fish lil nigga congrats")