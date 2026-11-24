<<<<<<< Updated upstream
from pathlib import Path

from django.http import FileResponse
from django.shortcuts import render

BUNDLE = Path(__file__).resolve().parent / "campus-gym.zip"
=======
from decimal import Decimal, InvalidOperation

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Max, Sum
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.utils.text import slugify
from django.views.decorators.http import require_POST

from .forms import ExerciseForm
from .library import MUSCLE_ORDER
from .models import Exercise, SetLog, Workout, WorkoutExercise, WorkoutSession
>>>>>>> Stashed changes


def home(request):
    return render(request, "gym/home.html", {"page": "home"})


<<<<<<< Updated upstream
def library(request):
    return render(request, "gym/placeholder.html", {"title": "Library", "page": "library"})


def gym_setup(request):
    return render(request, "gym/placeholder.html", {"title": "Gym", "page": "gym"})


def routines(request):
    return render(request, "gym/placeholder.html", {"title": "Routines", "page": "routines"})


def download_project(request):
    return FileResponse(BUNDLE.open("rb"), as_attachment=True, filename="campus-gym.zip")
=======
def _unique_slug(name):
    base = slugify(name)[:70] or "exercise"
    slug = base
    number = 2
    while Exercise.objects.filter(slug=slug).exists():
        slug = f"{base}-{number}"
        number += 1
    return slug


def _owned_workout(request, pk):
    return get_object_or_404(
        Workout.objects.prefetch_related("items__exercise"),
        pk=pk,
        student=request.user,
    )


def _count(value, fallback, low=1, high=30):
    try:
        number = int(value)
    except (TypeError, ValueError):
        return fallback
    return min(high, max(low, number))


def _weight(value):
    text = (value or "").strip()
    if not text:
        return None
    try:
        number = Decimal(text)
    except InvalidOperation:
        return None
    if number < 0:
        return None
    return min(number, Decimal("999.9"))


def _muscles_for(workout):
    seen = []
    for item in workout.items.all():
        muscle = item.exercise.muscle
        if muscle not in seen:
            seen.append(muscle)
    return seen


@login_required
def my_workouts(request):
    workouts = request.user.workouts.prefetch_related("items__exercise").annotate(
        exercise_count=Count("items")
    )
    cards = [{"workout": workout, "muscles": _muscles_for(workout)} for workout in workouts]
    return render(request, "gym/workouts.html", {"page": "workouts", "cards": cards})


@login_required
@require_POST
def create_workout(request):
    name = request.POST.get("name", "").strip()
    if not name:
        messages.error(request, "Give the workout a name.")
        return redirect("workouts")
    workout = Workout.objects.create(student=request.user, name=name[:80])
    return redirect("workout_builder", pk=workout.pk)


@login_required
def workout_builder(request, pk):
    workout = _owned_workout(request, pk)
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "delete":
            workout.delete()
            messages.success(request, "Workout deleted.")
            return redirect("workouts")
        if action == "duplicate":
            copy = Workout.objects.create(
                student=request.user,
                name=f"{workout.name} copy"[:80],
            )
            for item in workout.items.all():
                WorkoutExercise.objects.create(
                    workout=copy,
                    exercise=item.exercise,
                    sets=item.sets,
                    reps=item.reps,
                    weight=item.weight,
                    rest_seconds=item.rest_seconds,
                    position=item.position,
                )
            messages.success(request, "Workout duplicated.")
            return redirect("workout_builder", pk=copy.pk)
        if action == "remove":
            workout.items.filter(pk=request.POST.get("item")).delete()
            messages.success(request, "Exercise removed.")
            return redirect("workout_builder", pk=workout.pk)
        if action in {"up", "down"}:
            _move_item(workout, request.POST.get("item"), action)
            return redirect("workout_builder", pk=workout.pk)
        name = request.POST.get("name", "").strip()
        if not name:
            messages.error(request, "The workout name cannot be empty.")
            return redirect("workout_builder", pk=workout.pk)
        workout.name = name[:80]
        workout.save()
        for item in workout.items.all():
            item.sets = _count(request.POST.get(f"sets-{item.pk}"), item.sets)
            item.reps = _count(request.POST.get(f"reps-{item.pk}"), item.reps)
            item.rest_seconds = _count(
                request.POST.get(f"rest-{item.pk}"), item.rest_seconds, low=0, high=600
            )
            item.weight = _weight(request.POST.get(f"weight-{item.pk}"))
            item.save(update_fields=["sets", "reps", "rest_seconds", "weight"])
        messages.success(request, "Workout saved.")
        return redirect("workout_builder", pk=workout.pk)
    return render(
        request,
        "gym/workout_builder.html",
        {"page": "workouts", "workout": workout, "items": workout.items.all()},
    )


def _move_item(workout, item_id, direction):
    items = list(workout.items.all())
    index = next((i for i, item in enumerate(items) if str(item.pk) == str(item_id)), None)
    if index is None:
        return
    swap = index - 1 if direction == "up" else index + 1
    if swap < 0 or swap >= len(items):
        return
    current, other = items[index], items[swap]
    current.position, other.position = other.position, current.position
    if current.position == other.position:
        current.position = index
        other.position = swap
    current.save(update_fields=["position"])
    other.save(update_fields=["position"])


@login_required
def floor(request):
    if request.method == "POST" and request.POST.get("action") == "remove":
        exercise = get_object_or_404(Exercise, pk=request.POST.get("exercise"), is_custom=True)
        name = exercise.name
        if exercise.video:
            exercise.video.delete(save=False)
        exercise.delete()
        messages.success(request, f"Removed {name}.")
        return redirect("floor")
    form = ExerciseForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        exercise = form.save(commit=False)
        exercise.is_custom = True
        exercise.slug = _unique_slug(exercise.name)
        last = Exercise.objects.aggregate(last=Max("position"))["last"] or 0
        exercise.position = last + 1
        exercise.save()
        messages.success(request, f"Added {exercise.name}.")
        return redirect("floor")
    return render(
        request,
        "gym/floor.html",
        {
            "page": "floor",
            "form": form,
            "exercises": Exercise.objects.filter(is_custom=True),
        },
    )


def _filtered_exercises(request):
    exercises = Exercise.objects.all()
    muscle = request.GET.get("muscle", "").strip()
    equipment = request.GET.get("equipment", "").strip()
    difficulty = request.GET.get("difficulty", "").strip()
    query = request.GET.get("q", "").strip()
    muscles = [name for name in MUSCLE_ORDER if Exercise.objects.filter(muscle=name).exists()]
    extras = (
        Exercise.objects.exclude(muscle__in=MUSCLE_ORDER)
        .order_by("muscle")
        .values_list("muscle", flat=True)
        .distinct()
    )
    muscles.extend(extras)
    equipment_choices = list(
        Exercise.objects.order_by("equipment").values_list("equipment", flat=True).distinct()
    )
    difficulties = ["Beginner", "Intermediate", "Advanced"]
    if muscle in muscles:
        exercises = exercises.filter(muscle=muscle)
    else:
        muscle = ""
    if equipment in equipment_choices:
        exercises = exercises.filter(equipment=equipment)
    else:
        equipment = ""
    if difficulty in difficulties:
        exercises = exercises.filter(difficulty=difficulty)
    else:
        difficulty = ""
    if query:
        exercises = exercises.filter(name__icontains=query)
    return {
        "exercises": exercises,
        "muscles": muscles,
        "equipment_choices": equipment_choices,
        "difficulties": difficulties,
        "muscle": muscle,
        "equipment": equipment,
        "difficulty": difficulty,
        "query": query,
    }


@login_required
def exercise_library(request):
    context = _filtered_exercises(request)
    counts = {
        row["muscle"]: row["total"]
        for row in Exercise.objects.values("muscle").annotate(total=Count("id"))
    }
    groups = [
        {"name": name, "count": counts.get(name, 0)}
        for name in context["muscles"]
        if counts.get(name, 0)
    ]
    context.update({"page": "library", "groups": groups})
    return render(request, "gym/library.html", context)


@login_required
def exercise_detail(request, slug):
    exercise = get_object_or_404(Exercise, slug=slug)
    return render(
        request,
        "gym/exercise_detail.html",
        {"page": "library", "exercise": exercise},
    )


@login_required
def add_exercises(request, pk):
    workout = _owned_workout(request, pk)
    context = _filtered_exercises(request)
    if request.method == "POST":
        exercise = get_object_or_404(Exercise, pk=request.POST.get("exercise"))
        if not workout.items.filter(exercise=exercise).exists():
            last = workout.items.aggregate(last=Max("position"))["last"] or 0
            WorkoutExercise.objects.create(
                workout=workout,
                exercise=exercise,
                position=last + 1,
            )
            messages.success(request, f"Added {exercise.name}.")
        return redirect(request.get_full_path())
    context.update(
        {
            "page": "workouts",
            "workout": workout,
            "added_ids": set(workout.items.values_list("exercise_id", flat=True)),
        }
    )
    return render(request, "gym/exercise_catalog.html", context)


def _owned_session(request, pk):
    return get_object_or_404(
        WorkoutSession.objects.select_related("workout"),
        pk=pk,
        student=request.user,
    )


def _session_items(session):
    return list(session.workout.items.select_related("exercise"))


def _close_session(session, status):
    session.status = status
    session.finished_at = timezone.now()
    session.rest_until = None
    session.save(update_fields=["status", "finished_at", "rest_until"])


@login_required
@require_POST
def start_workout(request, pk):
    workout = _owned_workout(request, pk)
    items = _session_items_from_workout(workout)
    if not items:
        messages.error(request, "Add at least one exercise before you start.")
        return redirect("workout_builder", pk=workout.pk)
    active = (
        WorkoutSession.objects.filter(student=request.user, status=WorkoutSession.ACTIVE)
        .order_by("-started_at")
        .first()
    )
    if active and active.workout_id == workout.id:
        return redirect("live_workout", pk=active.pk)
    if active:
        _close_session(active, WorkoutSession.ABANDONED)
    first = items[0]
    session = WorkoutSession.objects.create(
        student=request.user,
        workout=workout,
        draft_reps=first.reps,
        draft_weight=first.weight,
    )
    return redirect("live_workout", pk=session.pk)


def _session_items_from_workout(workout):
    return list(workout.items.select_related("exercise"))


@login_required
def live_workout(request, pk):
    session = _owned_session(request, pk)
    if session.status != WorkoutSession.ACTIVE:
        return redirect("workout_summary", pk=session.pk)
    items = _session_items(session)
    if not items:
        _close_session(session, WorkoutSession.ABANDONED)
        messages.error(request, "This workout has no exercises.")
        return redirect("workouts")
    if session.exercise_index >= len(items):
        _close_session(session, WorkoutSession.FINISHED)
        return redirect("workout_summary", pk=session.pk)
    if request.method == "POST":
        return _handle_live_post(request, session, items)
    return render(request, "gym/session.html", _live_context(session, items))


def _wants_json(request):
    return request.headers.get("x-requested-with") == "fetch"


def _handle_live_post(request, session, items):
    action = request.POST.get("action")
    item = items[min(session.exercise_index, len(items) - 1)]
    if action == "reps":
        session.draft_reps = max(0, session.draft_reps + _count(request.POST.get("delta"), 0, low=-100, high=100))
        session.save(update_fields=["draft_reps"])
    elif action == "weight":
        session.draft_weight = _weight(request.POST.get("weight"))
        session.save(update_fields=["draft_weight"])
    elif action == "complete":
        _complete_set(session, items, item)
    elif action == "skip-rest":
        session.rest_until = None
        session.save(update_fields=["rest_until"])
    elif action == "add-rest":
        base = session.rest_until if session.rest_until and session.rest_until > timezone.now() else timezone.now()
        session.rest_until = base + timezone.timedelta(seconds=30)
        session.save(update_fields=["rest_until"])
    elif action == "goto":
        session.exercise_index = _count(request.POST.get("index"), session.exercise_index, low=0, high=len(items) - 1)
        session.rest_until = None
        _reset_draft(session, items[session.exercise_index])
    elif action == "edit-log":
        log = get_object_or_404(SetLog, pk=request.POST.get("log"), session=session)
        log.reps = _count(request.POST.get("reps"), log.reps, low=0, high=100)
        log.weight = _weight(request.POST.get("weight"))
        log.save(update_fields=["reps", "weight"])
    elif action == "end":
        done = _planned_sets(items)
        logged = session.logs.count()
        status = WorkoutSession.FINISHED if logged >= done and done else WorkoutSession.ABANDONED
        _close_session(session, status)
        return redirect("workout_summary", pk=session.pk)
    if session.status != WorkoutSession.ACTIVE:
        return redirect("workout_summary", pk=session.pk)
    if _wants_json(request):
        return JsonResponse({"reps": session.draft_reps, "rest": bool(session.rest_until)})
    return redirect("live_workout", pk=session.pk)


def _rest_deadline(seconds):
    if not seconds:
        return None
    return timezone.now() + timezone.timedelta(seconds=seconds)


def _planned_sets(items):
    return sum(item.sets for item in items)


def _reset_draft(session, item):
    done = session.logs.filter(item=item).count()
    session.draft_reps = 0 if done >= item.sets else item.reps
    session.draft_weight = item.weight
    session.save(update_fields=["exercise_index", "draft_reps", "draft_weight", "rest_until"])


def _complete_set(session, items, item):
    done = session.logs.filter(item=item).count()
    if done >= item.sets:
        return
    SetLog.objects.create(
        session=session,
        item=item,
        set_number=done + 1,
        reps=session.draft_reps,
        weight=session.draft_weight,
    )
    done += 1
    if done < item.sets:
        session.draft_reps = item.reps
        session.rest_until = _rest_deadline(item.rest_seconds)
        session.save(update_fields=["draft_reps", "rest_until"])
        return
    next_index = session.exercise_index + 1
    if next_index >= len(items):
        _close_session(session, WorkoutSession.FINISHED)
        return
    session.exercise_index = next_index
    session.rest_until = _rest_deadline(item.rest_seconds)
    following = items[next_index]
    session.draft_reps = following.reps
    session.draft_weight = following.weight
    session.save(update_fields=["exercise_index", "draft_reps", "draft_weight", "rest_until"])


def _live_context(session, items):
    index = min(session.exercise_index, len(items) - 1)
    item = items[index]
    logs = list(session.logs.filter(item=item))
    done = len(logs)
    resting = bool(session.rest_until and session.rest_until > timezone.now())
    total_sets = _planned_sets(items)
    logged_sets = session.logs.count()
    return {
        "page": "live",
        "session": session,
        "items": items,
        "item": item,
        "logs": logs,
        "set_number": min(done + 1, item.sets),
        "sets_done": done,
        "resting": resting,
        "rest_until": session.rest_until.isoformat() if session.rest_until else "",
        "rest_seconds": item.rest_seconds,
        "progress": int(logged_sets / total_sets * 100) if total_sets else 0,
        "logged_sets": logged_sets,
        "total_sets": total_sets,
    }


@login_required
def workout_summary(request, pk):
    session = _owned_session(request, pk)
    logs = session.logs.select_related("item__exercise")
    total_reps = sum(log.reps for log in logs)
    volume = Decimal("0")
    for log in logs:
        if log.weight:
            volume += log.weight * log.reps
    finished = session.finished_at or timezone.now()
    elapsed = finished - session.started_at
    minutes = int(elapsed.total_seconds() // 60)
    seconds = int(elapsed.total_seconds() % 60)
    return render(
        request,
        "gym/summary.html",
        {
            "page": "history",
            "session": session,
            "logs": logs,
            "total_reps": total_reps,
            "total_sets": logs.count(),
            "volume": volume,
            "minutes": minutes,
            "seconds": seconds,
        },
    )


@login_required
def history(request):
    sessions = (
        request.user.sessions.exclude(status=WorkoutSession.ACTIVE)
        .select_related("workout")
        .annotate(total_sets=Count("logs"), total_reps=Sum("logs__reps"))
    )
    return render(request, "gym/history.html", {"page": "history", "sessions": sessions})
>>>>>>> Stashed changes
