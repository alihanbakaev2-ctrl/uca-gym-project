from django.db import migrations

from gym.catalog import CAMPUS_EXERCISES


def seed_exercises(apps, schema_editor):
    Exercise = apps.get_model("gym", "Exercise")
    for position, (name, muscle, equipment, cue, video_id) in enumerate(CAMPUS_EXERCISES, start=1):
        Exercise.objects.update_or_create(
            video_id=video_id,
            defaults={
                "name": name,
                "muscle": muscle,
                "equipment": equipment,
                "cue": cue,
                "position": position,
            },
        )


def remove_exercises(apps, schema_editor):
    Exercise = apps.get_model("gym", "Exercise")
    video_ids = [row[4] for row in CAMPUS_EXERCISES]
    Exercise.objects.filter(video_id__in=video_ids).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("gym", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_exercises, remove_exercises),
    ]
