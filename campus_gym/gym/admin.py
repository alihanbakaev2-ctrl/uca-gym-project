from django.contrib import admin

from .models import Exercise, Workout, WorkoutExercise


class WorkoutExerciseInline(admin.TabularInline):
    model = WorkoutExercise
    extra = 0


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("name", "muscle", "equipment", "position")
    list_filter = ("muscle", "equipment")
    search_fields = ("name",)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("name", "student", "updated_at")
    search_fields = ("name", "student__username")
    inlines = [WorkoutExerciseInline]
