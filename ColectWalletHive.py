from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import numpy as np
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

os.chdir('/home/clautc/DataspellProjects/colectar_crypto_hive')

class ColectWalletHive:
    def __init__(self, metadata):
        self.metadata = metadata
        self.data = []

    def recorrer_tabla_paginada(self, driver, wait):
        if 'Next' in driver.find_element(By.CLASS_NAME, 'Paginator_root__uHZJM').text.split('\n'):
            next_ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.metadata['clase_next'])))
            filas = driver.find_elements(By.XPATH, self.metadata['xpath_data'])
            for f in filas:
                self.data.append(f.text.split('\n'))
            next_.click()
        else:
            filas = driver.find_elements(By.XPATH, self.metadata['xpath_data'])
            for f in filas:
                self.data.append(f.text.split('\n'))

        return self.data

    def obtener_transacciones(self):

        with open(self.metadata['path_wallet']) as file:
            for linea in file:
                driver = webdriver.Chrome(executable_path=self.metadata['path'])
                driver.get(self.metadata['website'])
                driver.maximize_window()
                wait = WebDriverWait(driver, 15)
                barra = driver.find_element(By.ID, self.metadata['id_ingreso_wallet_enter'])
                barra.send_keys(linea)
                barra.send_keys(Keys.ENTER)
                sleep(2)
                wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'CookieBarAnalytics-module-btn-2ZijD'))).click()
                sleep(5)
                wait.until(EC.element_to_be_clickable((By.XPATH, self.metadata['xpath_payouts']))).click()
                sleep(5)
                titulos = wait.until(EC.presence_of_element_located((By.XPATH, self.metadata['xpath_titles'])))
                encabezados = titulos.text.split('\n')
                datos = self.recorrer_tabla_paginada(driver, wait)
                driver.close()

        tabla = pd.DataFrame(datos, columns=encabezados)
        return tabla



