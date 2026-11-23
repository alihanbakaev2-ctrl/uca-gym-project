from pathlib import Path

from django.http import FileResponse
from django.shortcuts import render

BUNDLE = Path(__file__).resolve().parent / "campus-gym.zip"


def home(request):
    return render(request, "gym/home.html", {"page": "home"})


def library(request):
    return render(request, "gym/placeholder.html", {"title": "Library", "page": "library"})


def gym_setup(request):
    return render(request, "gym/placeholder.html", {"title": "Gym", "page": "gym"})


def routines(request):
    return render(request, "gym/placeholder.html", {"title": "Routines", "page": "routines"})


def download_project(request):
    return FileResponse(BUNDLE.open("rb"), as_attachment=True, filename="campus-gym.zip")
