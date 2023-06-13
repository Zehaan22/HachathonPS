# Solve for IITK

### The Problem

The problem we identified is the omnipresent issue of scheduling in campus life. In an environment where every individual is involved in such a large number of activities, it often becomes difficult for team leaders, project managers, secretaries, or coordinators of clubs to call meetings due to the large number of clashes they need to accommodate. Thus, in this problem statement, we solved two major issues that will streamline the process of scheduling.

1. We fixed the issue of compiling schedules of team members,
2. We created tools to optimise the process of setting a date and time for a given meet.

### The Solution

We created tools that not only help you schedule your day in a structured and well-curated manner but also helps teams and clubs schedule their meets easily without individually consulting all their team members.

These tools can be integrated eventually with a UI that automatically integrates academic schedule from pingala and to which a user can manually add time commitments.

A user will have a unique user-id that you can share with your team leaders/ Club coordinators who can create teams with your user-ids. Our algorithms will help them schedule a time for any meets that they are planning on having based on whether they want a set number of people to show up or whether they want to meet up at a specific time.

This would be really helpful for the campus junta as this addresses a really widespread issue and is a relatable problem for most of the junta.

### The How

We’ll be using Python as the main programming language for solving this problem.

The main algorithms for optimising the availability will be written in a module named “Optimiser” with the algorithms for each being written in separate files.
The files would be :
Opt_number (For picking a time that optimizes number of people available)
Opt_time(For checking how many people are available at a given time)

### Future of this solution:

We plan to integrate Pingala into this app for the automatic inclusion of students academic calender and academic commitments into the time table and help us make this app dynamic.

The user_id will be replaced by student’s role number and faculty id for the faculty.

The user interface will be shifted to a basic webpage built using react.js and backend code shifted to Django with SQLlite framework.
