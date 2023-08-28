from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def responseTest(request):
    return HttpResponse('it is what is is')