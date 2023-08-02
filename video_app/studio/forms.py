from django import forms

from .models import Video


class UploadVideo(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["videoFile", "subtitleFile", "title"]
