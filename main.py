from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\ASUS\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'

driver = webdriver.Chrome(options=options)

driver.get('https://apps5.mineco.gob.pe/transparencia/Navegador/default.aspx?y=2023&ap=Proyecto')

# WebDriverWait(driver, 5)\
#     .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
#                                       'button.didomi-components-button didomi-button didomi-dismiss-button didomi-components-button--color didomi-button-highlight highlight-button'.replace(' ', '.'))))\
#     .click()

# WebDriverWait(driver, 5)\
#     .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
#                                       'input#term')))\
#     .send_keys('Madrid')

try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'ctl00_CPH1_BtnTipoGobierno'))).click()
except TimeoutException:
    print("Tiempo de espera agotado. El elemento no es interactuable.")
except NoSuchElementException:
    print("No se pudo encontrar el elemento en la página.")
except Exception as e:
    print(f"Error desconocido: {e}")

# WebDriverWait(driver, 5)\
#     .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
#                                       'i.icon_weather_s.icon.icon-local')))\
#     .click()

# WebDriverWait(driver, 25)\
#     .until(EC.element_to_be_clickable((By.XPATH,
#                                       '/html/body/div[8]/div[1]/div[4]/div/main/section[3]/section/div/div/table')))

# texto_columnas = driver.find_element(By.XPATH, '/html/body/div[8]/div[1]/div[4]/div/main/section[3]/section/div/div/table')
# texto_columnas = texto_columnas.text
# print(texto_columnas)


# WebDriverWait(driver, 5)\
#     .until(EC.element_to_be_clickable((By.XPATH,
#                                       '/html/body/div[7]/main/div[4]/div/section[4]/section/div[1]/ul')))

# texto_columnas = driver.find_element_by_xpath('/html/body/div[7]/main/div[4]/div/section[4]/section/div[1]/ul')
# texto_columnas = texto_columnas.text

# tiempo_hoy = texto_columnas.split('Mañana')[0].split('\n')[1:-1]

# horas = list()
# temp = list()
# v_viento = list()

# for i in range(0, len(tiempo_hoy), 4):
#     horas.append(tiempo_hoy[i])
#     temp.append(tiempo_hoy[i+1])
#     v_viento.append(tiempo_hoy[i+2])

# df = pd.DataFrame({'Horas': horas, 'Temperatura': temp, 'V_viento(km_h)':v_viento})
# print(df)
# df.to_csv('tiempo_hoy.csv', index=False)

# driver.quit()