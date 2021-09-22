from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .calendarAPI import events, connect
from .Scripts import read_colles

colors = {
 'SI': "#D5C404",
 'Maths': "#0415D5",
 'Phy': "#C404D5",
 'Ang': "#D5047E",
 'Fr': "#7DD504",
 'Red': "#D50415",
}

"""def index(request):
    # colle
    colle_dict = events.colle_by_matiere()
    colle = "<h1>les khôlles</h1>"
    for matiere, desc in colle_dict.items():
        colle += "<p><h2>"+matiere+"</h2>"+desc+"</p>"

    # taf
    events_dict = events.homework_by_day()
    taf = "<h1>le taf</h1>"
    last = ""  # si y a 2h il va y avoir 2 events pareil
    for date, _events in events_dict.items():
        taf += "<h2>%s</h2>"%date
        for event in _events:
            # untuple
            date, title, desc = event
            desc = connect.CleanStr(desc)

            taf += "<p>"+title+": "+desc+"</p>"

    return HttpResponse("Hello, world. You're at the polls index."+colle+taf)"""
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