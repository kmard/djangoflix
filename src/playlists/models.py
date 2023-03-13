from django.db import models
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from videos.models import Video
from django.db.models.signals import pre_save
from src.djangoflix.db.models import PublishStateOptions
from src.djangoflix.db.receivers import publish_state_pre_save,slugify_pre_save

class PlaylistQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(
            state=PublishStateOptions.PUBLISH,
            publish_timestamp__lte=now
        )


class PlaylistManager(models.Manager):
    def get_queryset(self):
        return PlaylistQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()


class PublishStateOptions(models.TextChoices):
    PUBLISH = 'PU', 'Published'
    DRAFT = 'DR', 'Draft'
    UNLISTED = 'UN', 'Unlisted'
    Private = 'PR', 'Private'


class Playlist(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    video = models.ForeignKey(Video,null=True,on_delete=models.SET_NULL) #one video per playlist
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    state = models.CharField(max_length=2, choices=PublishStateOptions.choices, default=PublishStateOptions.DRAFT)
    publish_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)

    objects = PlaylistManager()

pre_save.connect(publish_state_pre_save, sender=Playlist)
pre_save.connect(slugify_pre_save, sender=Playlist)