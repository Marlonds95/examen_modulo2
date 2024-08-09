from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep

df = pd.read_csv('datos/datos.csv')

df2 = pd.read_csv('datos/datosPago.csv')

driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/index.html")
sleep(5)


formulario = driver.find_element(By.XPATH, '/html/body/nav/div[1]/ul/li[8]/a')
formulario.click()
sleep(1)

# ##

for index, fila in df.iterrows():

      nombre = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/form/div[1]/input') 
      nombre.send_keys(fila['Nombre'])

      password = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/form/div[2]/input') 
      password.send_keys(fila['Password'])
    

      ingresar = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/button[2]')
      ingresar.click()
      sleep(1)

      alert = driver.switch_to.alert 
     
      alert.accept()

login = driver.find_element(By.XPATH, '/html/body/nav/div[1]/ul/li[5]/a')
login.click()
sleep(1)

for index, fila in df.iterrows():

      nombre = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[1]/input') 
      nombre.send_keys(fila['Nombre'])

      password = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[2]/input') 
      password.send_keys(fila['Password'])
    

      ingresar = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]')
      ingresar.click()
      sleep(3)

         
compra = driver.find_element(By.LINK_TEXT, 'Samsung galaxy s6')
compra.click()
sleep(2)

aceptar = driver.find_element(By.LINK_TEXT, 'Add to cart')
aceptar.click()
sleep(2)

alert = driver.switch_to.alert 
alert.accept()
sleep(2)

regreso = driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[1]/a')
regreso.click()
sleep(1)

compra2 = driver.find_element(By.LINK_TEXT, 'Nokia lumia 1520')
compra2.click()
sleep(2)

aceptar = driver.find_element(By.LINK_TEXT, 'Add to cart')
aceptar.click()
sleep(2)

alert = driver.switch_to.alert 
alert.accept()
sleep(2)

carrito = driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[4]/a')
carrito.click()
sleep(1)

pago = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/button')
pago.click()
sleep(1)

for index, fila in df2.iterrows():

      nombre = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[1]/input') 
      nombre.send_keys(fila['Nombre'])

      pais = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[2]/input') 
      pais.send_keys(fila['Pais'])

      ciudad = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[3]/input') 
      ciudad.send_keys(fila['Ciudad'])

      tarjeta = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[4]/input') 
      tarjeta.send_keys(fila['Tarjeta'])

      mes = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[5]/input') 
      mes.send_keys(fila['Mes'])

      ano = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[6]/input') 
      ano.send_keys(fila['Ano'])
    

      ingresar = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]')
      ingresar.click()
      sleep(3)

      alert_button = driver.find_element(By.XPATH, "/html/body/div[10]/div[7]/div/button")
      alert_button.click()
      sleep(2)


cerrarSesion = driver.find_element(By.XPATH, '/html/body/nav/div[1]/ul/li[6]/a')
cerrarSesion.click()
sleep(3)

# # Cerrar el driver
driver.quit()