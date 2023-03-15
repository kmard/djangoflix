from django.contrib import admin

from .models import VideoAllProxy,VideoPublishedProxy

class VideoAllAdmin(admin.ModelAdmin):
    list_display = ['title','slug','video_id','state','active','get_playlist_ids']
    search_fields = ['title',]
    list_filter = ['title','active','state']
    readonly_fields = ['publish_timestamp', 'get_playlist_ids']
    class Meta:
        model = VideoAllProxy

admin.site.register(VideoAllProxy,VideoAllAdmin)

class VideoPublishedProxyAdmin(admin.ModelAdmin):
    list_display = ['title','slug','video_id','active','get_playlist_ids']
    search_fields = ['title',]
    list_filter = ['title','video_id']
    class Meta:
        model = VideoPublishedProxy

    def get_queryset(self,request):
        return VideoPublishedProxy.objects.filter(active=True)

admin.site.register(VideoPublishedProxy,VideoPublishedProxyAdmin)
