
import json
from ColectWalletHive import *
from functions import *

"""
el objetivo de este script es crear una tabla con transacciones del mes
"""

# ejemplo metadata
# metadata = {
#     'website': 'https://hiveon.net/eth/payouts',
#     'path': '/usr/bin/chromedriver_linux/chromedriver',
#     'path_wallet': '/home/user/Projects/project/carpeta/archivo.txt',
#     'id_ingreso_wallet_enter': 'wallet-address',
#     'xpath_payouts': '//*[@id="tabs-nav"]/div/div[3]',
#     'xpath_titles': '//*[@id="rc-tabs-0-panel-0"]//*[contains(@class, "PayoutsStyles_row__OXAxB PayoutsStyles_header__KC0pz")]',
#     'xpath_data': '//*[@id="rc-tabs-0-panel-0"]//*[contains(@class, "PayoutsStyles_row__OXAxB PayoutsStyles_dataRow__HKZYm")]',
#     'xpath_siguiente': '//*[@id="rc-tabs-0-panel-0"]/div[2]/div[2]/button[2]',
#     'clase_next': "Paginator_btnNext___hYCT"
# }

insumo_path = '/home/clautc/DataspellProjects/colectar_crypto_hive/otros/otros.txt'

if os.path.exists(insumo_path):
    with open(insumo_path) as f:
        path = f.readline()

if os.path.exists(path):
    with open(path) as f:
        metadata = json.load(f)

h = ColectWalletHive(metadata)
df = h.obtener_transacciones()

# procesar data bruta

df = modificar_variables_datetime(df, 'Time')
df = extraer_string_moneda(df, 'Total')

df.columns = df.columns.str.lower()
df = df.drop(['transaction'], axis=1)

df_produccion_mensual = analisis_produccion_mensual(df)
produccion_mensual = df_produccion_mensual.reset_index()

# guardar data procesada

crear_dir_data()
df.to_feather('data/df_hive.feather')
produccion_mensual.to_feather('data/df_produccion_mensual.feather')

#%%
