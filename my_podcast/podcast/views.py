from django.http import HttpResponse
from django.template import loader
from .models import Podcast

def podcasts(request):
    podcasts = Podcast.objects.all().values()
    template = loader.get_template('all_podcasts.html')
    context = {
        'mypodcasts': podcasts,
    }
    return HttpResponse(template.render(context, request))
