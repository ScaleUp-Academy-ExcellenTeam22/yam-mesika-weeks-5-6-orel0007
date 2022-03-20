
import datetime
import random


def random_date_in_range_str(start, end):
    """
    The function choose random date in the range between the 2 given dates
    :param start: start date - String!!!
    :param end: end date - String!!!
    :return: random date between the 2 dates
    """
    list_dates = []
    list_dates = start.split("-")
    start_date = datetime.date(int(list_dates[0]), int(list_dates[1]), int(list_dates[2]))
    list_dates = end.split("-")
    end_date = datetime.date(int(list_dates[0]), int(list_dates[1]), int(list_dates[2]))
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    if(int(random_date.isoweekday()) == 1):
        # check if the day is monday, isoweekday() return the num of the day referring monday is 1 and move on...
        print("אין לי ויניגרט!")
    return random_date


print(random_date_in_range_str("1912-06-23", "1954-06-07"))
