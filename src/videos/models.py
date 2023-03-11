from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

class VideoQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(
                state = Video.VideoStateOptions.PUBLISH,
                publish_timestamp__lte=now
        )


class VideoManager(models.Manager):
    def get_queryset(self):
        return VideoQuerySet(self.model,using=self._db)

    def published(self):
        return self.get_queryset().published()

class Video(models.Model):

    class VideoStateOptions(models.TextChoices):
        PUBLISH = 'PU','Published'
        DRAFT = 'DR', 'Draft'
        UNLISTED = 'UN', 'Unlisted'
        Private = 'PR', 'Private'


    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=50,unique=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=False,blank=True,null=True)
    updated = models.DateTimeField(auto_now_add=False,blank=True,null=True)
    state = models.CharField(max_length=2, choices=VideoStateOptions.choices,default=VideoStateOptions.DRAFT)
    publish_timestamp = models.DateTimeField(auto_now_add=False,auto_now=False,blank=True,null=True)


    objects =  VideoManager()

    def save(self,*args,**kwargs):
        if self.state == self.VideoStateOptions.PUBLISH and self.publish_timestamp is None:
            # print('save as timestamp for published')
            self.publish_timestamp = timezone.now()
        elif self.state == self.VideoStateOptions.DRAFT :
            self.publish_timestamp = None

        if self.slug is None:
            self.slug = slugify(self.title)

        super().save(* args, ** kwargs)



class VideoPublishedProxy(Video):
    class Meta:
        proxy = True
        verbose_name='Published Video'
        verbose_name_plural = 'Published Videos'

class VideoAllProxy(Video):
    class Meta:
        proxy = True
        verbose_name='All Video'
        verbose_name_plural = 'All Videos'