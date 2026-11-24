from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
<<<<<<< Updated upstream
    path("library/", views.library, name="library"),
    path("gym/", views.gym_setup, name="gym_setup"),
    path("routines/", views.routines, name="routines"),
    path("download/campus-gym.zip", views.download_project, name="download_project"),
=======
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
    path("library/", views.exercise_library, name="library"),
    path("library/<slug:slug>/", views.exercise_detail, name="exercise_detail"),
    path("history/", views.history, name="history"),
    path("workouts/new/", views.create_workout, name="create_workout"),
    path("workouts/<int:pk>/", views.workout_builder, name="workout_builder"),
    path("workouts/<int:pk>/exercises/", views.add_exercises, name="add_exercises"),
    path("workouts/<int:pk>/start/", views.start_workout, name="start_workout"),
    path("sessions/<int:pk>/", views.live_workout, name="live_workout"),
    path("sessions/<int:pk>/summary/", views.workout_summary, name="workout_summary"),
>>>>>>> Stashed changes
]
