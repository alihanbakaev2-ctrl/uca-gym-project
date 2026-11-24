from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Max
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import ExerciseForm
from .models import Exercise, Workout, WorkoutExercise


def home(request):
    if request.user.is_authenticated:
        return redirect("workouts")
    return redirect("login")


@login_required
def my_workouts(request):
    workouts = request.user.workouts.annotate(exercise_count=Count("items"))
    return render(
        request,
        "gym/workouts.html",
        {"page": "workouts", "workouts": workouts},
    )


@login_required
@require_POST
def create_workout(request):
    number = request.user.workouts.count() + 1
    name = "New workout" if number == 1 else f"New workout {number}"
    workout = Workout.objects.create(student=request.user, name=name)
    return redirect("workout_builder", pk=workout.pk)


def _owned_workout(request, pk):
    return get_object_or_404(Workout, pk=pk, student=request.user)


def _count(value, fallback):
    try:
        number = int(value)
    except (TypeError, ValueError):
        return fallback
    return min(30, max(1, number))


@login_required
def workout_builder(request, pk):
    workout = _owned_workout(request, pk)
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "delete":
            workout.delete()
            return redirect("workouts")
        if action == "remove":
            workout.items.filter(pk=request.POST.get("item")).delete()
            messages.success(request, "Exercise removed.")
            return redirect("workout_builder", pk=workout.pk)
        name = request.POST.get("name", "").strip()
        workout.name = name[:80] or "New workout"
        workout.save()
        for item in workout.items.all():
            item.sets = _count(request.POST.get(f"sets-{item.pk}"), item.sets)
            item.reps = _count(request.POST.get(f"reps-{item.pk}"), item.reps)
            item.save(update_fields=["sets", "reps"])
        messages.success(request, "Workout saved.")
        return redirect("workout_builder", pk=workout.pk)
    return render(
        request,
        "gym/workout_builder.html",
        {
            "page": "workouts",
            "workout": workout,
            "items": workout.items.select_related("exercise"),
        },
    )


@login_required
def floor(request):
    if request.method == "POST" and request.POST.get("action") == "remove":
        exercise = get_object_or_404(Exercise, pk=request.POST.get("exercise"))
        name = exercise.name
        exercise.video.delete(save=False)
        exercise.delete()
        messages.success(request, f"Removed {name}.")
        return redirect("floor")
    form = ExerciseForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        exercise = form.save(commit=False)
        last = Exercise.objects.aggregate(last=Max("position"))["last"] or 0
        exercise.position = last + 1
        exercise.save()
        messages.success(request, f"Added {exercise.name}.")
        return redirect("floor")
    return render(
        request,
        "gym/floor.html",
        {"page": "floor", "form": form, "exercises": Exercise.objects.all()},
    )


@login_required
def add_exercises(request, pk):
    workout = _owned_workout(request, pk)
    muscle = request.GET.get("muscle", "").strip()
    exercises = Exercise.objects.all()
    muscles = list(Exercise.objects.order_by("muscle").values_list("muscle", flat=True).distinct())
    if muscle and muscle in muscles:
        exercises = exercises.filter(muscle=muscle)
    else:
        muscle = ""
    if request.method == "POST":
        exercise = get_object_or_404(Exercise, pk=request.POST.get("exercise"))
        already = workout.items.filter(exercise=exercise).exists()
        if not already:
            last = workout.items.aggregate(last=Max("position"))["last"] or 0
            WorkoutExercise.objects.create(
                workout=workout,
                exercise=exercise,
                position=last + 1,
            )
            messages.success(request, f"Added {exercise.name}.")
        return redirect(request.get_full_path())
    added_ids = set(workout.items.values_list("exercise_id", flat=True))
    return render(
        request,
        "gym/exercise_catalog.html",
        {
            "page": "workouts",
            "workout": workout,
            "exercises": exercises,
            "muscles": muscles,
            "muscle": muscle,
            "added_ids": added_ids,
        },
    )
