from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path(
        "login/",
        LoginView.as_view(
            template_name="gym/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("workouts/", views.my_workouts, name="workouts"),
    path("floor/", views.floor, name="floor"),
    path("workouts/new/", views.create_workout, name="create_workout"),
    path("workouts/<int:pk>/", views.workout_builder, name="workout_builder"),
    path("workouts/<int:pk>/exercises/", views.add_exercises, name="add_exercises"),
]
