from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("library/", views.library, name="library"),
    path("gym/", views.gym_setup, name="gym_setup"),
    path("routines/", views.routines, name="routines"),
    path("download/campus-gym.zip", views.download_project, name="download_project"),
]
