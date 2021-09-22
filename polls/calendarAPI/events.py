from .connect import get_events
import datetime

colors = {
 'SI': "#D5C404",
 'Maths': "#0415D5",
 'Phy': "#C404D5",
 'Ang': "#D5047E",
 'Fr': "#7DD504",
 'Red': "#D50415",
}
def mat2color(matiere):
    if "MATH" in matiere.upper():
        return colors['Maths']
    if "PHY" in matiere.upper():
        return colors['Phy']
    if "SI" in matiere.upper():
        return colors['SI']
    if "FR" in matiere.upper():
        return colors['Fr']
    if "ANG" in matiere.upper():
        return colors['Ang']

def homework_by_day():
    """
    events = {
    "demain (20/09)":[tuple_event, tuple_event],
    "le 21/09":[tuple_event,]
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
        if event_day == int(today.day)+1:
            if "demain, le %s"%date in events:
                events["demain, le %s"%date].append(event_tuple)
            else:
                events["demain, le %s"%date] = [event_tuple]
        # si c'est pas aujourd'hui
        else:
            if "le %s"%date in events:
                events["le %s"%date].append(event_tuple)
            else:
                events["le %s"%date] = [event_tuple]
        last = desc
    return events


def colle_by_matiere():
    """
    events = {matiere: desciption}
    """
    events_list = get_events(5)
    events = {}
    for event in events_list:
        # untuple
        _date, titre, desc = event
        color = mat2color(titre)
        if ("khôlle" in titre) or ("kholle" in titre) or ("colle" in titre):
            if "SI" in titre:
                events["Science de l'ingénieur"] = (desc, color)
            elif "Phy" in titre:
                events["Physique"] = (desc, color)
            elif "math" in titre:
                events["Maths"] = (desc, color)
            else:
                events[titre] = (desc, color)
    return events

