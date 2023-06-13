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

Table description for User
[('id', b'int', 'NO', 'PRI', None, 'auto_increment'), 
('user_name', b'varchar(255)', 'YES', '', None, ''), 
('address', b'varchar(255)', 'YES', '', None, ''), 
('Events', b'json', 'YES', '', None, ''), 
('teams', b'json', 'YES', '', None, '')]
"""
import mysql.connector as sql
import datetime
import json

mydb = sql.connect(
    host="localhost",
    user="root",
    password="Zattak@321",
    database="TimePlanner"
)

cursor = mydb.cursor()


class Event:
    """Acts as the node for the events iterable (events) for User."""

    def __init__(self, user_id, desc, date, time):
        self.user_id = user_id  # The user who has this event
        self.event_desc = desc  # String description of the event
        self.date = date  # Date of the event
        self.time = time  # Duration of the event


class Team:
    """Acts as the interable object to store the team members and team leads."""

    def __init__(self, name, members, leaders, team_id):
        self.id = team_id  # Variable to store the unique team id
        self.name = name  # String for team name
        self.members = members  # List of members(User[])
        self.leaders = leaders  # List of leaders(User[])


class User:
    """The main object upon which all structures are based."""

    def __init__(self, name):
        self.id = None  # Variable to strore the unique user_id
        self.name = name  # String of user name
        self.events = json.dumps([])  # List to store the events
        self.teams = json.dumps([])  # List of teams that the user is in

        # Add the user to the database
        self.add_user_to_databse()

    def add_event(self, event):
        command = ("SELECT events FROM User WHERE id = %s")
        vals = (self.id)
        cursor.execute(command, vals)
        events_array = cursor.fetchall()
        adding_tupe = (event.event_desc, event.date, event.time)
        events_array.append(adding_tupe)

        self.events = json.dumps(events_array)

        command2 = ("UPDATE user SET events = %s WHERE id = %s")
        vals = (self.events, self.id)
        cursor.execute(command2, vals)
        mydb.commit()

    def check_events(self):
        command = ("SELECT events FROM User WHERE id = %s")
        vals = (self.id)
        cursor.execute(command, vals)
        events_array = cursor.fetchall()
        print(events_array)

    def add_user_to_databse(self):
        """Add the user to the database."""
        command = "INSERT INTO User (user_name,teams) VALUES (%s,%s)"
        vals = (self.name, self.teams)
        cursor.execute(command, vals)
        mydb.commit()

        command = "SELECT id FROM User WHERE user_name = %s"
        vals = (self.name,)
        cursor.execute(command, vals)

        x = cursor.fetchall()
        self.id = x[0]


foo = User("del")

event = Event(foo.id, "My Birthday", "2023/07/08/2300", 2)
foo.add_event(event)
foo.check_events()
