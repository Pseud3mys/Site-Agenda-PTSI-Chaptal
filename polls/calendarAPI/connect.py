import datetime
from googleapiclient.discovery import build

dev_Key = "AIzaSyDiE-XzamHeDBZO9icSIvCIx7m4Xwx5IBE"


def get_events(nbr_events=25, time_max=False):
    service = build('calendar', 'v3', developerKey=dev_Key)
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    if not time_max:
        events_result = service.events().list(calendarId='ptsi.chaptal@gmail.com', timeMin=now, singleEvents=True,
                                          maxResults=nbr_events, orderBy='startTime').execute()
    else:
        events_result = service.events().list(calendarId='ptsi.chaptal@gmail.com', timeMin=now, timeMax=time_max, singleEvents=True,
                                          maxResults=nbr_events, orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        return None
    events_list = []
    for event in events:
        date = event['start'].get('dateTime', event['start'].get('date'))
        date = date[2:10]
        date = date[6:8]+"/"+date[3:5]
        summary = event['summary'] if 'summary' in event else "No summary"
        description = event['description'] if 'description' in event else "No description"

        events_list.append((date,summary,description))
        #print("%s -- %s:\n     %s\n" % (date_obj, summary, description))
    return events_list