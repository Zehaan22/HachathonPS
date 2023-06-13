"""File to optimise the time for a given number of members or leaders."""


def wrt_members(min_members, team, pref_date, duration, pref_time=None):
    """Optimises a meet time with refernce to the min number of members required."""

    for i in range(24):
        available_members = 0

        if pref_time:
            curr_time = pref_time
        else:
            pref_time = i
        for member in team.members:
            for event in member.events:
                if event.date == pref_date:
                    # 15 min buffer
                    if event.time in range(curr_time-0.25, curr_time+duration+0.25):
                        break
            else:
                available_members += 1

        if available_members >= min_members:
            return curr_time

    return False  # No such time found change date


def wrt_leaders(min_leaders, team, pref_date, duration, pref_time=None):
    """Optimises a meet time with refernce to the min number of members required."""

    for i in range(24):
        available_leaders = 0

        if pref_time:
            curr_time = pref_time
        else:
            pref_time = i
        for member in team.leaders:
            for event in member.events:
                if event.date == pref_date:
                    # 15 min buffer
                    if event.time in range(curr_time-0.25, curr_time+duration+0.25):
                        break
            else:
                available_leaders += 1

        if available_leaders >= min_leaders:
            return curr_time

    return False  # No such time found change date
