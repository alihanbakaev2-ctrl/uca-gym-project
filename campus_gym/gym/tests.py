from django.test import TestCase

<<<<<<< Updated upstream
# Create your tests here.
=======
from gym.models import Exercise, WorkoutExercise


def clip(name="squat.mp4"):
    return SimpleUploadedFile(name, b"fake-video", content_type="video/mp4")


class WorkoutFlowTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.student = User.objects.create_user("alikhan", password="gymfloor")
        cls.exercise = Exercise.objects.create(
            name="Barbell back squat",
            muscle="Quads",
            equipment="Barbell",
            cue="Sit down and stand up.",
            video=clip(),
        )

    def test_home_sends_students_to_login(self):
        response = self.client.get(reverse("home"))
        self.assertRedirects(response, reverse("login"))

    def test_sign_in_opens_my_workouts(self):
        self.client.login(username="alikhan", password="gymfloor")
        response = self.client.get(reverse("home"))
        self.assertRedirects(response, reverse("workouts"))
        page = self.client.get(reverse("workouts"))
        self.assertContains(page, "My Workouts")
        self.assertContains(page, "Create workout")

    def test_student_can_add_a_campus_exercise(self):
        self.client.login(username="alikhan", password="gymfloor")
        created = self.client.post(reverse("create_workout"), {"name": "Push Day"})
        workout_id = created.url.rstrip("/").split("/")[-1]
        builder = reverse("workout_builder", args=[workout_id])
        self.assertRedirects(created, builder)

        catalog = reverse("add_exercises", args=[workout_id])
        listing = self.client.get(catalog)
        self.assertContains(listing, "Barbell back squat")
        self.assertContains(listing, "video")

        added = self.client.post(catalog, {"exercise": self.exercise.pk})
        self.assertRedirects(added, catalog)
        self.assertEqual(WorkoutExercise.objects.filter(workout_id=workout_id).count(), 1)

        page = self.client.get(builder)
        self.assertContains(page, "Barbell back squat")

    def test_floor_keeps_only_uploaded_exercises(self):
        self.client.login(username="alikhan", password="gymfloor")
        response = self.client.post(
            reverse("floor"),
            {
                "name": "Campus row",
                "muscle": "Back",
                "equipment": "Cable",
                "cue": "Pull to the ribs.",
                "video": clip("row.mp4"),
            },
        )
        self.assertRedirects(response, reverse("floor"))
        self.assertTrue(Exercise.objects.filter(name="Campus row").exists())

    def test_library_covers_each_muscle_group(self):
        from gym.library import MUSCLE_ORDER

        for muscle in MUSCLE_ORDER:
            self.assertGreaterEqual(Exercise.objects.filter(muscle=muscle, is_custom=False).count(), 15)

    def test_live_counter_never_goes_negative_and_saves_history(self):
        self.client.login(username="alikhan", password="gymfloor")
        created = self.client.post(reverse("create_workout"), {"name": "Leg Day"})
        workout_id = created.url.rstrip("/").split("/")[-1]
        self.client.post(
            reverse("add_exercises", args=[workout_id]),
            {"exercise": self.exercise.pk},
        )
        item = WorkoutExercise.objects.get(workout_id=workout_id)
        item.sets = 1
        item.save(update_fields=["sets"])
        started = self.client.post(reverse("start_workout", args=[workout_id]))
        session_url = started.url
        self.client.post(session_url, {"action": "reps", "delta": "-20"})
        from gym.models import WorkoutSession

        session = WorkoutSession.objects.get(pk=session_url.rstrip("/").split("/")[-1])
        self.assertEqual(session.draft_reps, 0)
        self.client.post(session_url, {"action": "complete"})
        self.assertContains(self.client.get(reverse("history")), "Leg Day")
>>>>>>> Stashed changes
