from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Playlist
from videos.models import Video
from src.djangoflix.db.models import PublishStateOptions
from django.utils import timezone
from django.utils.text import slugify


class PlaylistModelTestCase(TestCase):
    # python manage.py test playlists

    def setUp(self):
        video_a = Video.objects.create(title = 'My title',video_id = 'abc12')
        self.video_a = video_a
        self.obj_a = Playlist.objects.create(title="This is my title",video = self.video_a
                                             )

        self.obj_b = Playlist.objects.create(title="This is my title",video = self.video_a,
                             state = PublishStateOptions.PUBLISH,
                             )

    def test_playlist_video(self):
        self.assertEqual(self.obj_a.video, self.video_a)

    # def test_video_playlist_ids_property(self):
    #     ids = self.obj_a.get_playlist_ids()
    #     actual_ids = list(Playlist.objects.filter(video =  self.video_a).values_list('id',flat=True))
    #     self.assertEqual(ids, actual_ids)

    def test_video_playlist(self):
       qs = self.video_a.playlist_featured.all()
       self.assertTrue(qs.count() == 2)


    def test_slug_field(self):
        title = self.obj_a.title
        test_slug = slugify(title)
        self.assertEqual(test_slug,self.obj_a.slug)

    def test_valid_title(self):
        title = 'This is my title'
        qs = Playlist.objects.filter(title=title)
        self.assertEqual(qs.exists(),True)

    def test_created_count(self):
        qs = Playlist.objects.all()
        self.assertEqual(qs.count(),2)

    def test_publish_case(self):
        now = timezone.now()
        qs = Playlist.objects.filter(state = PublishStateOptions.PUBLISH,publish_timestamp__lte = now)
        self.assertEqual(qs.exists(),True)

    def test_draft_case(self):
        qs = Playlist.objects.filter(state = PublishStateOptions.DRAFT)
        self.assertEqual(qs.count(),1)

    def test_publish_manager(self):
       published_qs = Playlist.objects.all().published()
       published_qs_2 = Playlist.objects.published()
       self.assertTrue(published_qs.exists())
       self.assertEqual(published_qs.count(),published_qs_2.count())