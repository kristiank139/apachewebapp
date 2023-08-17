from django.shortcuts import render
from django.http import HttpResponse
from django import get_version

# Create your views here.

def index(request):

    return HttpResponse("Running django " + get_version())