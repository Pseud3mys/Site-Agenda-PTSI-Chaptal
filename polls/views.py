from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .calendarAPI import events
from .Scripts import read_colles
from .Scripts.global_tool import colors


def index(request):
    template = loader.get_template('index.html')
    context = {
        'colors': colors
    }
    return HttpResponse(template.render(context, request))

def taf(request):
    template = loader.get_template('taf.html')
    events_dict = events.homework_by_day()
    context = {
        'dict_taf': events_dict
    }
    return HttpResponse(template.render(context, request))

def colles(request):
    if request.method=="GET":
        groupe = request.GET.get("Sgroupe")
        if groupe is None:
            groupe = "9"
    template = loader.get_template('colles.html')
    colle_dict = events.colle_by_matiere()
    colloscope = read_colles.get_colles(int(groupe))
    context = {
        'colle_dict': colle_dict,
        'colloscope': colloscope,
        'num_groupe': groupe
    }
    return HttpResponse(template.render(context, request) + str(request))


