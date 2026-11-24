import django.db.models.deletion
from django.db import migrations, models


def clear_stock_exercises(apps, schema_editor):
    WorkoutExercise = apps.get_model("gym", "WorkoutExercise")
    Exercise = apps.get_model("gym", "Exercise")
    WorkoutExercise.objects.all().delete()
    Exercise.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("gym", "0002_seed_exercises"),
    ]

    operations = [
        migrations.RunPython(clear_stock_exercises, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name="exercise",
            name="video_id",
        ),
        migrations.AddField(
            model_name="exercise",
            name="video",
            field=models.FileField(upload_to="exercises/"),
        ),
        migrations.AlterField(
            model_name="exercise",
            name="cue",
            field=models.CharField(blank=True, max_length=180),
        ),
        migrations.AlterField(
            model_name="workoutexercise",
            name="exercise",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="placements",
                to="gym.exercise",
            ),
        ),
    ]
