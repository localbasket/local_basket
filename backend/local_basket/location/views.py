from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def homepage(requests):
    return HttpResponse('<h1> This is the homepage of location app</h1>')
