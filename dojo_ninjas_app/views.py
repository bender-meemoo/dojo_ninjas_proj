from django.shortcuts import render, HttpResponse
from .models import Dojo
# Create your views here.

def index(request):
    return HttpResponse('Yo what is up!')
