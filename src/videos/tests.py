from django.test import TestCase
from .models import Video
from django.utils import timezone


class VideoModelTestCase(TestCase):
    # python manage.py test videos

    def setUp(self):
        Video.objects.create(title="This is my title")
        Video.objects.create(title="This is my title", state = Video.VideoStateOptions.PUBLISH)


    def test_valid_title(self):
        title = 'This is my title'
        qs = Video.objects.filter(title=title)
        self.assertEqual(qs.exists(),True)

    def test_created_count(self):
        qs = Video.objects.all()
        self.assertEqual(qs.count(),2)

    def test_publish_case(self):
        now = timezone.now()
        qs = Video.objects.filter(state = Video.VideoStateOptions.PUBLISH,publish_timestamp__lte = now)
        self.assertEqual(qs.exists(),True)

    def test_draft_case(self):
        qs = Video.objects.filter(state = Video.VideoStateOptions.DRAFT)
        self.assertEqual(qs.count(),1)

