# wheel/views.py
import random
from django.http import JsonResponse
from django.shortcuts import render
from .models import SpinResult

PRIZES = ["10 Coins", "Try Again", "50 Coins", "100 Coins", "No Prize", "Jackpot"]

def spin_page(request):
    return render(request, 'wheel/spin.html')

def spin_wheel(request):
    if request.method == "POST":
        prize = random.choice(PRIZES)
        user = request.POST.get("user", "Anonymous")
        SpinResult.objects.create(user=user, prize=prize)
        return JsonResponse({"status": "ok", "prize": prize})
    return JsonResponse({"status": "fail"})
