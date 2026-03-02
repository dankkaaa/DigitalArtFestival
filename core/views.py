from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignupForm


def home(request):
    return render(request, "core/home.html")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")   # можно заменить на /registrations/my/
    else:
        form = SignupForm()

    return render(request, "registration/signup.html", {"form": form})