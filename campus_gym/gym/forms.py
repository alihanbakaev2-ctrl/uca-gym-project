from django import forms
from django.core.exceptions import ValidationError

from .models import Exercise


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ["name", "muscle", "equipment", "cue", "video"]
        labels = {
            "cue": "Coaching cue",
            "video": "Your video",
        }
        widgets = {
            "video": forms.ClearableFileInput(attrs={"accept": "video/mp4,video/webm,video/quicktime"}),
        }

    def clean_video(self):
        video = self.cleaned_data["video"]
        if video and video.size > 80 * 1024 * 1024:
            raise ValidationError("Use a video under 80 MB.")
        return video
