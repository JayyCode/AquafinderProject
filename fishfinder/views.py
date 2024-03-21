from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def search (resquest):
    return HttpResponse("Search Engine")

def home_dashboard(request):
    return HttpResponse("Welcome Home Nigga")

def products(request):
    return HttpResponse("this is the general products page")

def detail_view(request):
    return HttpResponse("this is the detailed page for products")

def signup(request):
    return HttpResponse("type ya info in lil nigga")

def login(request):
    return HttpResponse("who is u lil niggha log in")

def watchlist(request):
    return HttpResponse("this ya watch list lil nigga")

def adminview(request):
    return HttpResponse("its time to ban niggas folk")