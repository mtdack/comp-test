from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    params = {
        'title':'Hello There!',
        'msg':'next page',
        'next':'next1'
    }
    return render(request, 'next/index.html', params)

def next1(request):
    params = {
        'title':'Hello There!',
        'msg':'next1 page',
        'next': 'next2'
    }
    return render(request, 'next/index.html', params)

def next2(request):
    params = {
        'title':'Hello There!',
        'msg':'next2 pase',
        'next': 'index'
    }
    return render(request, 'next/index.html', params)