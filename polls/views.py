from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.


def hello(request):
    return HttpResponse("hello world")

def get_time(request):
    now=f"it is now {time.localtime()}"     
    return HttpResponse(now)