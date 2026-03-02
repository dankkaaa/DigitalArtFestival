import random
from django.shortcuts import render
from django.http import JsonResponse

def stage(request):
    return render(request, "generative/stage.html")

def seed_api(request):
    return JsonResponse({"seed": random.randint(1, 9999999)})