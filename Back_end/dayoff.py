import datetime as dt
import calendar
import pandas as pd
import nurse
import general_functions

def month_generator():
    date = dt.date.today()
    last_day = calendar.monthrange(date.year, date.month)[1]
    days = [day for day in range(1, last_day + 1)]

    df = nurse.read_nurse()
    df = df[df['Data Exclusão'].isnull()]
    df = pd.DataFrame(columns=days, index=df['Nome'].to_list())

    sundays = []
    for day in range(1, last_day+1):
        temp = dt.date(date.year, date.month, day)
        temp = general_functions.week(temp)

        if temp == 'D':
            sundays.append(day)

    df[sundays] = 2
    df.fillna(0, inplace=True)

    df.to_csv(f'./db/dayoff/{calendar.month_name[date.month]}-{date.year}.csv'.lower())


def read_month(month_year):
    return pd.read_csv(f'./db/dayoff/{calendar.month_name[month_year[0]]}-{month_year[1]}.csv'.lower(), index_col=[0])


def set_dayoff(row, column, month_year):
    df = read_month(month_year)
    resignated = nurse.read_nurse()
    resignated = resignated.loc[resignated['Data Exclusão'].notnull(), 'Nome'].tolist()

    if df.iloc[row].name in resignated:
        return 1

    if dt.date(month_year[1], month_year[0], column+1) >= dt.date.today():
        if df.iloc[row, column] == 0 or df.iloc[row, column] == 2:
            df.iloc[row, column] = 1

        elif general_functions.week(dt.date(month_year[1], month_year[0], column+1)) == 'D':
            df.iloc[row, column] = 2

        else:
            df.iloc[row, column] = 0

        df.to_csv(f'./db/dayoff/{calendar.month_name[month_year[0]]}-{month_year[1]}.csv'.lower())

    else:
        return 1
