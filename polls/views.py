from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from polls.models import Sujet

from .calendarAPI import events
from .Scripts import read_colles
from .Scripts.global_tool import colors, matiere_list


def index(request):
    template = loader.get_template('index.html')
    context = {
        'colors': colors
    }
    return HttpResponse(template.render(context, request))

def taf(request):
    template = loader.get_template('taf.html')
    events_dict = events.homework_by_day()
    num_semaine = events.get_num_semaine()
    context = {
        'dict_taf': events_dict,
        'num_semaine': num_semaine,
    }
    return HttpResponse(template.render(context, request))

def colles(request):
    if request.method=="GET":
        groupe = request.GET.get("Sgroupe")
        if groupe is None:
            groupe = "9"
    template = loader.get_template('colles.html')
    colle_dict = events.colle_by_matiere()
    colloscope, num_semaine = read_colles.get_colles(int(groupe))
    #num_semaine = events.get_num_semaine()
    context = {
        'colle_dict': colle_dict,
        'colloscope': colloscope,
        'num_groupe': groupe,
        'num_semaine':  "Semaine "+num_semaine,
    }
    return HttpResponse(template.render(context, request) + str(request))

def sujets(request):
    template = loader.get_template('sujets.html')
    sujet_list = Sujet.objects.order_by('-pub_date')[:20]
    # choix matiere
    if request.method=="GET":
        selected_matiere = request.GET.get("Smatiere")
        if selected_matiere == "All":
            sujet_list = Sujet.objects.order_by('-pub_date')[:20]
        elif selected_matiere:
            sujet_list = Sujet.objects.filter(matiere=selected_matiere).order_by('-pub_date')[:10]
    # parse
    context = {
        "latest_sujet_list": sujet_list,
        "matiere_list": matiere_list,
        "val_selected": selected_matiere,
    }
    return HttpResponse(template.render(context, request) + str(request))
