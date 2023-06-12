"""File to create the objects required for the files.

We have:
events
{
user_id = int
event_desc = string
event_date = date
event_time = date.hrs()
}

team
{
leader_ids = list(int)
member_ids = list(int)
}

user
{
user_id = int
events = list(events)
teams = list(team)
}
"""
import mysql.connector as sql

mydb = sql.connect(
    host = "localhost",
    user="root",
    password="Zattak@321",
    database = "TimePlanner"
)

cursor = mydb.cursor()



class Event:
    """Acts as the node for the events iterable (events) for User."""

    def __init__(self, user_id , desc , date ,time):
        self.user_id = user_id #The user who has this event
        self.event_desc = desc #String description of the event
        self.date = date #Date of the event
        self.time = time #Time of the event
        
    
class Team:
    """Acts as the interable object to store the team members and team leads."""
    
    def __init__(self,name, members, leaders, team_id):
        self.id = team_id # Variable to store the unique team id
        self.name = name # String for team name
        self.members = members # List of members(User[])
        self.leaders = leaders # List of leaders(User[])
        
    
class User:
    """The main object upon which all structures are based."""
    
    def __init__(self, user_id, name, events, teams):
        self.id = user_id # Variable to strore the unique user_id
        self.name = name # String of user name
        self.events = events # List to store the events
        self.teams = teams # List of teams that the user is in
   
    def add_event(self, event):
        self.events.append(event)