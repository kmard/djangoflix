from django.test import TestCase
from .models import Video


class VideoModelTestCase(TestCase):
    # python manage.py test videos

    def setUp(self):
        Video.objects.create(title="This is my title")

    def test_valid_title(self):
        title = "This is my title"
        qs = Video.objects.filter(title=title)
        self.assertEqual(qs.exists())
