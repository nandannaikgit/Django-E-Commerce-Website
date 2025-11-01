from django.shortcuts import render

# Create your views here.

def services(request):
    return HttpResponse("<h1> This is service page </h1>")
