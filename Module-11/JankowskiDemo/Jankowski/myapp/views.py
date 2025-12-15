from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("Jankowski says HELLO!!")


# Create your views here.
