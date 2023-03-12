from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save
from src.djangoflix.db.models import PublishStateOptions
from src.djangoflix.db.receivers import publish_state_pre_save,slugify_pre_save


# Create your models here.
# class PublishStateOptions(models.TextChoices):
#     PUBLISH = 'PU', 'Published'
#     DRAFT = 'DR', 'Draft'
#     UNLISTED = 'UN', 'Unlisted'
#     Private = 'PR', 'Private'


class VideoQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(
            state=PublishStateOptions.PUBLISH,
            publish_timestamp__lte=now
        )


class VideoManager(models.Manager):
    def get_queryset(self):
        return VideoQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()


class PublishStateOptions(models.TextChoices):
    PUBLISH = 'PU', 'Published'
    DRAFT = 'DR', 'Draft'
    UNLISTED = 'UN', 'Unlisted'
    Private = 'PR', 'Private'


class Video(models.Model):


    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=50, unique=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    state = models.CharField(max_length=2, choices=PublishStateOptions.choices, default=PublishStateOptions.DRAFT)
    publish_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)

    objects = VideoManager()

    # def save(self, *args, **kwargs):
    #
    #     # if self.slug is None:
    #     #     self.slug = slugify(self.title)
    #
    #     super().save(*args, **kwargs)


class VideoPublishedProxy(Video):
    class Meta:
        proxy = True
        verbose_name = 'Published Video'
        verbose_name_plural = 'Published Videos'


class VideoAllProxy(Video):
    class Meta:
        proxy = True
        verbose_name = 'All Video'
        verbose_name_plural = 'All Videos'


# def publish_state_pre_save(sender, instance, *args, **kwargs):
#     is_publish = instance.state == PublishStateOptions.PUBLISH
#     is_draft = instance.state == PublishStateOptions.DRAFT
#
#     if is_publish and instance.publish_timestamp is None:
#         # print('save as timestamp for published')
#         instance.publish_timestamp = timezone.now()
#     elif is_draft:
#         instance.publish_timestamp = None


pre_save.connect(publish_state_pre_save, sender=Video)


# def slugify_pre_save(sender,instance,*args,**kwargs):
#     title = instance.title
#     slug = instance.slug
#     if slug is None:
#         instance.slug = slugify(title)

pre_save.connect(slugify_pre_save, sender=Video)