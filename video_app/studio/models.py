from django.db import models
from django.conf import settings


class Video(models.Model):
    title = models.CharField(max_length=60, blank=False)
    videoFile = models.FileField(upload_to='uploads')
    subtitleFile = models.FileField(upload_to='uploads')
    uploaded_date = models.DateTimeField()
    
    # link to the user that uploaded the image
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"Video<{self.id}>"
