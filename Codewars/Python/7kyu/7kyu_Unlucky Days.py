from datetime import date
import calendar


def unlucky_days(year):

    counter = 0

    for x in range(1, 13):
        given_date = date(year, x, 13)
        if calendar.day_name[given_date.weekday()] == "Friday":
            counter += 1

    return counter
