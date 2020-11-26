import pandas as pd
import datetime as dt

def formulary_generator(funcionario, acamados, pacientes):
    df = pd.DataFrame(columns=['Enfermeiro', 'Aux/Tec Enfermagem', 'Escriturário', 'N° acamados', 'N° pacientes'],
                      index=['1°CD', '2°CD', '3°CD', '4°CD', '5°CD', '6°CD', '7°CD', '2°HOSP', '3°HOSP',
                             '1°Oneday', '2°Oneday', '3°Oneday', '1°BLOCO A']
                      )
    df['Enfermeiro'] = funcionario
    df['N° acamados'] = acamados
    df['N° pacientes'] = pacientes

    df.to_csv(f'./db/forms/formulario_{dt.datetime.now().date()}.csv', index=False)


def read_formulary(day_month_year):
    return pd.read_csv(f"./db/forms/formulario_{day_month_year[2]}-{day_month_year[1] if day_month_year[1] > 9 else '0' + str(day_month_year[1])}-{day_month_year[0] if day_month_year[0] > 9 else '0' + str(day_month_year[0])}.csv")

