import requests
from ics import Calendar
from datetime import datetime, timedelta

# Define a function to retrieve the calendar.
def next_week_events(url):
    response = requests.get(url)
    ics_file = response.text
    c = Calendar(ics_file)
    now = datetime.now()
    next_week = now + timedelta(weeks=1)

# Iterate through the events.
    events = []
    for event in c.events:
        if event.begin.date() >= now.date() and event.begin.date() <= next_week.date():
            events.append(event)
    
# Print the results.
    if len(events) == 0:
        print("No events next week.")
    else:
        for event in events:
            print(event.name + " on " + str(event.begin.date()) + " at " + str(event.begin.time()))

# Pass a URL
next_week_events('')
