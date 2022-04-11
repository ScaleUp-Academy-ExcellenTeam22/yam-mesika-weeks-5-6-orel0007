import datetime
import random


def print_if_not_vinogret(num):
    if num == 1:
        # Check if the day is monday, isoweekday() return the num of the day referring monday is 1 and move on...
        print("אין לי ויניגרט!")


def random_date_between_2_dates(date1, date2):
    """
    The function chooses a random date.
    :param date1: start date - the first range date.
    :param date2: end date - the second range date.
    :return: random date between the 2 dates.
    """
    list_dates = []
    list_dates = date1.split("-")
    start_date = datetime.date(int(list_dates[0]), int(list_dates[1]), int(list_dates[2]))
    list_dates = date2.split("-")
    end_date = datetime.date(int(list_dates[0]), int(list_dates[1]), int(list_dates[2]))
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    # Check if the day is monday, if it is print  אין לי ויניגרט!
    print_if_not_vinogret(random_date.isoweekday())
    return random_date


if __name__ == '__main__':
    print(random_date_between_2_dates("1912-06-23", "1954-06-07"))
