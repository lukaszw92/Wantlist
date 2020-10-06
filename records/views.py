from django.shortcuts import render
from django.http import JsonResponse

def apiOverview(request):
    return JsonResponse("Dzieńdobry", safe=False)
