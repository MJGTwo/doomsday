"""Quizing doomsday algorithm."""
import click
import datetime
import random

numberToDay = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}


def weekday(number):
    """Convert isoformat weekday to human reable."""
    return numberToDay.get(number, "Invalid input")


def revealDayOfWeek(dateString):
    """Take in a string in isoformat and return the day of that week."""
    date = datetime.date.fromisoformat(dateString)
    return weekday(date.weekday())


def randomDate(start, end):
    """Return a date randomly in the middle of two dates given."""
    print("Start:", start)
    print("End:", end)
    return start + (end - start) * random.random()


@click.command()
@click.option('--reveal', default="", help="A date that you want to know  \
the weekday of.")
@click.option('--start', default="1980-01-01", help='Start date.')
@click.option('--end', default="2030-12-31", help='End date.')
def main(reveal, start, end):
    """Start the program."""
    if (reveal != ""):
        print(revealDayOfWeek(reveal))
    else:

        startDate = datetime.date.fromisoformat(start)
        endDate = datetime.date.fromisoformat(end)
        newDate = randomDate(startDate, endDate)
        print(newDate)


if __name__ == '__main__':
    main()
