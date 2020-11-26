import pandas as pd
import dayoff
import datetime as dt
import calendar
import general_functions

def read_nurse():
    return pd.read_csv('./db/nurses/nurses.csv')


def new_nurse(nome, setor):
    nurses = read_nurse()

    if not nurses.empty:
        if nome + setor not in nurses.apply(lambda x: x['Nome'] + x['Setor'], axis=1).to_list():
            cadastro = {'Nome': nome, 'Setor': setor, 'Data Cadastro': dt.date.today(), 'Data Exclusão': ''}
            nurses = nurses.append(cadastro, ignore_index=True)
            nurses.to_csv('./db/nurses/nurses.csv', index=False)

            insert = dayoff.read_month([dt.date.today().month, dt.date.today().year])
            insert = insert.append(pd.DataFrame(index=[nome], columns=insert.columns).fillna(0))
            for day in range(1, calendar.monthrange(dt.date.today().year, dt.date.today().month)[1]+1):
                if general_functions.week(dt.date(dt.date.today().year, dt.date.today().month ,day)) == 'D':
                    insert.loc[nome, str(day)] = 2

            insert.to_csv(f'./db/dayoff/{calendar.month_name[dt.datetime.now().month]}-{dt.datetime.now().year}.csv'.lower())

        else:
            return 1
        
    else:
        cadastro = {'Nome': nome, 'Setor': setor, 'Data Cadastro': dt.datetime.now().date(), 'Data Exclusão': ''}
        nurses = nurses.append(cadastro, ignore_index=True)
        nurses.to_csv('./db/nurses/nurses.csv', index=False)

        insert = dayoff.read_month([dt.datetime.now().month, dt.datetime.now().year])
        insert = insert.append(pd.DataFrame(index=[nome], columns=insert.columns).fillna(0))
        insert.to_csv(f'./db/dayoff/{calendar.month_name[dt.datetime.now().month]}-{dt.datetime.now().year}.csv'.lower())


def resignate_nurse(to_remove):
    df = read_nurse()

    if not df.empty:
        today = dt.datetime.now().date()
        x = df['Nome'] == to_remove
        y = 'Data Exclusão'
        df.loc[x, y] = today
        df.to_csv('./db/nurses/nurses.csv', index=False)

