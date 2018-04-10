import datetime

date = datetime.date.today()


def get_datetime_url():

    day = str(date.day)
    month = str(date.month)
    year = str(date.year)

    if len(month) != 2:
        month = str(0) + month

    if len(day) != 2:
        day = str(0) + day

    return year + month + day
