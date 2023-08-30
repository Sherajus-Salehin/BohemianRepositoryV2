from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def responseTest(request):
    return render(request, 'tmp1.html', {'position': 'manager'})
