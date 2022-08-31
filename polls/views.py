from django.shortcuts import render, HttpResponse,redirect


def index(request):
    return HttpResponse("Welcome,to Django page")


def login(request):
    return render(request, 'login.html')