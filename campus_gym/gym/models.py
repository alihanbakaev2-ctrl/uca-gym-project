from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=120, unique=True)
    muscle = models.CharField(max_length=40)
    equipment = models.CharField(max_length=40)
    cue = models.CharField(max_length=180, blank=True)
    video = models.FileField(
        upload_to="exercises/",
        validators=[FileExtensionValidator(["mp4", "webm", "mov"])],
    )
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position", "name"]

    def __str__(self):
        return self.name


class Workout(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="workouts",
    )
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return self.name


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(
        Workout,
        on_delete=models.CASCADE,
        related_name="items",
    )
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        related_name="placements",
    )
    sets = models.PositiveSmallIntegerField(default=3)
    reps = models.PositiveSmallIntegerField(default=8)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position", "id"]
        constraints = [
            models.UniqueConstraint(
                fields=["workout", "exercise"],
                name="one_exercise_per_workout",
            )
        ]

    def __str__(self):
        return f"{self.exercise.name} in {self.workout.name}"
