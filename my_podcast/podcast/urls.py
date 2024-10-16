from django.urls import path
from . import views

urlpatterns = [
    path('mypodcast/',views.podcasts, name='podcast'),
    path('mypodcast/detail/<int:id>/',views.details, name='details'),
    path('',views.main, name='main'),
    path('testing/', views.testing, name='testing'),
]
