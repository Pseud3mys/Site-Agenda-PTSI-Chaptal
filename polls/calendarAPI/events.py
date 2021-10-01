from .connect import get_events
import datetime
from ..Scripts.global_tool import mat2color, text2mat, num2day, CleanStr


def homework_by_day():
    """
    events = {
    "demain, le Mardi 20/09":[tuple_event, tuple_event],
    "Mardi 21/09":[tuple_event,]
    }
    """
    events_list = get_events(200)
    today = datetime.datetime.now()
    last = ""  # si y a 2h il va y avoir 2 events pareil
    events = {}
    for event in events_list:
        # untuple
        date, title, desc = event
        color = mat2color(title)
        event_tuple = (date, title, desc, color)
        # petit trie
        if desc == "No description" or desc==last:
            continue
        if ("khôlle" in title) or ("kholle" in title) or ("colle" in title):
            continue

        event_day = int(date[0:2])  # "20/09" -> 20
        day_of_colle = datetime.datetime.strptime(date+"/"+str(today.year), '%d/%m/%Y')
        date_str = "%s %s"%(num2day[day_of_colle.weekday()], date)

        # On prend le taf de today+1
        if event_day == int(today.day)+1:
            tomorrow_date_str = "%s (demain)"%date_str
            if tomorrow_date_str  in events:
                events[tomorrow_date_str].append(event_tuple)
            else:
                events[tomorrow_date_str] = [event_tuple]
        # si c'est pas aujourd'hui
        else:
            if date_str in events:
                events[date_str].append(event_tuple)
            else:
                events[date_str] = [event_tuple]
        last = desc
    return events


def colle_by_matiere():
    """
    events = {matiere: desciption}
    """
    """now = datetime.datetime.utcnow().isoformat() # test tmp max
    delta = datetime.timedelta(hours=10)
    nowDelta = now + delta"""
    events_list = get_events(nbr_events=3)
    events = {}
    for event in events_list:
        # untuple
        _date, titre, desc = event
        print(desc)
        color = mat2color(titre)
        if ("khôlle" in titre) or ("kholle" in titre) or ("colle" in titre):
            if text2mat(titre):
                if text2mat(titre) is not events:
                    events[text2mat(titre)] = (desc, color)
            else:
                if titre is not events:
                    events[titre] = (desc, color)
    return events

