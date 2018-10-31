from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.


def index(request):
    response = HttpResponse()
    response['a'] = 1
    return JsonResponse({
        "a" :1
    })