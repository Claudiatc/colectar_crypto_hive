import pandas as pd
import os
import errno

def crear_dir_data():
    try:
        os.mkdir('data')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

def modificar_variables_datetime(df, var):
    """
    :param df:
    :param var: format='%b %d, %Y, %I:%M %p EJ: Aug 09, 2021, 3:05 AM
    :return: df con variables origen convertida y creadas year + month
    """
    df[var] = pd.to_datetime(pd.to_datetime(df[var], format='%b %d, %Y, %I:%M %p'))
    df['month'] = df[var].dt.month_name()
    df['year'] = df[var].dt.year

    return df


def extraer_string_moneda(df, var):
    """
    :param df:
    :param var: variable origen de total
    :return: df con variables modificada a numérica y creada nombre moneda
    """
    df['moneda'] = df[var].str.extract(r'([A-Z]+)')
    df[var] = df[var].str.extract(r'(\d*\.\d*)')
    df[var] = pd.to_numeric(df[var])

    return df


def analisis_produccion_mensual(df):
    """
    :param df:
    :return: df2 con análisis de producción mensual considerando solo las transacciones exitosas
    """

    # 1) filtrar status "Transaction Succeed"
    df = df[df.status.str.contains(r'Succeed')]

    # 2) sumar producción por mes
    df_prod_mensual = df.groupby(['year', 'month']).total.agg(sum)

    # 3) consolidar incluyendo mes en español y guardar en feather

    print(df_prod_mensual)
    return df_prod_mensual


#%%
