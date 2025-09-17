from django.shortcuts import render, HttpResponse


def print_hello(request):
    return HttpResponse("Hello World")