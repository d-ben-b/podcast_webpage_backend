from django.urls import path
from . import views

urlpatterns = [
    path('mypodcast/',views.podcasts, name='podcast')
]
