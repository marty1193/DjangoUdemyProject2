from django.shortcuts import render
from django.urls import reverse
from django.http import Http404
from django.http import HttpResponse, HttpResponseNotAllowed


# Create your views here.
def starting_page(request):
    return render(request, "blog/index.html")
    

def posts(request):
    pass

def post_detail(request):
    pass