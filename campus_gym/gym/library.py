import json
from pathlib import Path

from django.db import IntegrityError, transaction

DATA_PATH = Path(__file__).resolve().parent / "data" / "exercises.json"
MUSCLE_ORDER = [
    "Chest",
    "Back",
    "Shoulders",
    "Biceps",
    "Triceps",
    "Forearms",
    "Quads",
    "Hamstrings",
    "Glutes",
    "Calves",
    "Abs/Core",
    "Full Body",
    "Cardio",
]


def load_entries():
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


def sync_library():
    from .models import Exercise

    entries = load_entries()
    with transaction.atomic():
        for index, entry in enumerate(entries):
            defaults = {
                "name": entry["name"],
                "muscle": entry["primary"],
                "secondary": ", ".join(entry.get("secondary") or []),
                "equipment": entry["equipment"],
                "difficulty": entry["difficulty"],
                "cue": "\n".join(entry.get("cues") or []),
                "is_custom": False,
                "position": index,
            }
            try:
                Exercise.objects.update_or_create(slug=entry["id"], defaults=defaults)
            except IntegrityError:
                continue
