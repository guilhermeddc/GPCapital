from django.contrib import admin
from app_gp.forms import *
from app_gp.utils.admin.widgets.VideoShow import VideoShowWidget


class VideoForm(ModelForm):

    class Meta:
        model = ClientVideo
        fields = ('video', )
        widgets = {
            'video': VideoShowWidget()
        }


class TabularClientVideos(admin.TabularInline):
    model = ClientVideo
    form = VideoForm
    extra = 0
