import datetime as dt

def week(day):
    dayw = ['S', 'T', 'Q', 'Q', 'S', 'S', 'D']
    return dayw[day.weekday()]
