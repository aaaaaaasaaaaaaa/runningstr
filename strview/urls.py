from django.urls import path
from . import views

urlpatterns = [
    path('videolist', views.VideoListView.as_view(), name='videolist'),
    path('create/<str:stringrun>', views.runtext, name='runtext'),
    path('', views.base, name='base')
]