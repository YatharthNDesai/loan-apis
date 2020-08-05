from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("First ever view.")

def second(request):
    return HttpResponse("Second option")

# Create your views here.
