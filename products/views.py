from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello world')


def newproduct(request):
    return HttpResponse('New product')