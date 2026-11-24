from django.db import models

<<<<<<< Updated upstream
# Models stay empty until we decide the app logic.
=======

class Exercise(models.Model):
    slug = models.SlugField(max_length=80, unique=True, null=True, blank=True)
    name = models.CharField(max_length=120, unique=True)
    muscle = models.CharField(max_length=40)
    secondary = models.CharField(max_length=160, blank=True)
    equipment = models.CharField(max_length=40)
    difficulty = models.CharField(max_length=20, blank=True)
    cue = models.TextField(blank=True)
    video = models.FileField(
        upload_to="exercises/",
        blank=True,
        validators=[FileExtensionValidator(["mp4", "webm", "mov"])],
    )
    is_custom = models.BooleanField(default=True)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position", "name"]

    def __str__(self):
        return self.name

    @property
    def cue_lines(self):
        return [line.strip() for line in self.cue.splitlines() if line.strip()]

    @property
    def secondary_list(self):
        if not self.secondary:
            return []
        return [part.strip() for part in self.secondary.split(",") if part.strip()]


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
    weight = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)
    rest_seconds = models.PositiveSmallIntegerField(default=90)
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


class WorkoutSession(models.Model):
    ACTIVE = "active"
    FINISHED = "finished"
    ABANDONED = "abandoned"
    STATUS_CHOICES = [
        (ACTIVE, "Active"),
        (FINISHED, "Finished"),
        (ABANDONED, "Ended early"),
    ]

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sessions",
    )
    workout = models.ForeignKey(
        Workout,
        on_delete=models.CASCADE,
        related_name="sessions",
    )
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=ACTIVE)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    exercise_index = models.PositiveIntegerField(default=0)
    draft_reps = models.PositiveSmallIntegerField(default=0)
    draft_weight = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)
    rest_until = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-started_at"]

    def __str__(self):
        return f"{self.workout.name} session"


class SetLog(models.Model):
    session = models.ForeignKey(
        WorkoutSession,
        on_delete=models.CASCADE,
        related_name="logs",
    )
    item = models.ForeignKey(
        WorkoutExercise,
        on_delete=models.CASCADE,
        related_name="logs",
    )
    set_number = models.PositiveSmallIntegerField()
    reps = models.PositiveSmallIntegerField()
    weight = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)

    class Meta:
        ordering = ["item__position", "set_number"]
        constraints = [
            models.UniqueConstraint(
                fields=["session", "item", "set_number"],
                name="one_log_per_set",
            )
        ]
>>>>>>> Stashed changes
