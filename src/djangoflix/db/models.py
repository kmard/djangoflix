from django.db import models

# Create your models here.
class PublishStateOptions(models.TextChoices):
    PUBLISH = 'PU', 'Published'
    DRAFT = 'DR', 'Draft'
    UNLISTED = 'UN', 'Unlisted'
    Private = 'PR', 'Private'