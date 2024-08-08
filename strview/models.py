from django.db import models

# Create your models here.
class VideoStorage(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title

