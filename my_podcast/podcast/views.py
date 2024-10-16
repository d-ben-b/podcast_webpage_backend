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
def details(request, id):
    template = loader.get_template('details.html')
    context = {
        'mypodcasts': Podcast.objects.get(id=id)
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['apple', 'banana', 'cherry','dog']
    }
    return HttpResponse(template.render(context, request))