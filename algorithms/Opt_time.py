from datetime import datetime, timedelta

def Opt_time(team,time):
    number = 0
    for user in team.members:
        for event in user.events:
            if time not in (event.date, event.date +_timedelta(hours = event.time)):
                            number += 1
    return number