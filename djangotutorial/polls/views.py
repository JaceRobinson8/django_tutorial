from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse(
        "To my wonderful husband: you are kind, funny, warm, and have a nice duck."
    )
