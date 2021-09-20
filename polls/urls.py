from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('taf', views.taf),
    path('colles', views.colles),
]