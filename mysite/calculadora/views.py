from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to the new calculator")


# Create your views here.
def add(request, a, b):
    return HttpResponse("La suma de "+str(a)+" + "+str(b)+" = "+str(a + b))


def subtract(request, a, b):
    return HttpResponse("La resta de "+str(a)+" - "+str(b)+" = "+str(a - b))


def multiply(request, a, b):
    return HttpResponse("La multiplicación de "+str(a)+" * "+str(b)+" = "+str(a * b))

