from django.contrib import admin
from .models import Podcast

# Register your models here.
class PodcastAdmin(admin.ModelAdmin):
  list_display = ('title', 'version', 'record_time')

admin.site.register(Podcast, PodcastAdmin)
