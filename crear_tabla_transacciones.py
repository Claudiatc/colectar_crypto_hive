from ColectWalletHive import *

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

with open('otros/otro.txt') as f:
    path = f.readline()

with open(path) as f:
    metadata = f.read()

h = ColectWalletHive(metadata)
df = h.obtener_transacciones()
