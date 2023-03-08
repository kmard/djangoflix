from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=50)
    # timestamp
    # updated
    # state
    # publish_timestamp

class VideoProxy(Video):
    class Meta:
        proxy = True
        verbose_name='Published Video'
        verbose_name_plural = 'Published Videos'