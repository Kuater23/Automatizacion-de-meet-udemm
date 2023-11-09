import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


option = Options()



driver = webdriver.Chrome()
driver.get("https://accounts.google.com/v3/signin/identifier?_ga=2.69552665.844164917.1699281914-725758107.1699281914&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&ec=asw-meet-globalnav-signin&ifkv=AVQVeyxEnTJID-uvorI-s30EUfIGAbrIk1qsY0z67bui7HX8haIXdIlyCGG7Fnz_uoKfxr0Yrxb1&ltmpl=meet&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-838466166%3A1699294000074215&theme=glif")
driver.maximize_window()
driver.execute("setPermissions", {"descriptor": {"name": "camera"}, "state": "granted"})
driver.execute("setPermissions", {"descriptor": {"name": "microphone"}, "state": "granted"})
#driver.add_credential(
#    "examenesvirtuales@udemm.edu.ar",
 #   "Examen-0520",
#)
#BUSCA EL INPUT DEL MAIL

usuario = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"identifierId")))
#MANDA EL MAIL AL INPUT ENCONTRADO

usuario.send_keys("examenesvirtuales@udemm.edu.ar")

#BUSCA EL BOTON DE CONTINUAR
nextEmail = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"identifierNext")))
nextEmail.click()

#BUSCA INPUT MAIL
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME,"Passwd")))
#MANDA LA CONTRASEÑA AL INPUT ENCONTRADO
password.send_keys('Examen-0520')

#SIGUIENTE PASO
nextPass = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID,"passwordNext")))
nextPass.click()

#ESPERA 5 SEGUNDOS
time.sleep(5)

#INGRESA EL CODIGO DE LA CLASE
codigo_clase = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID,"i8")))
codigo_clase.click()
codigo_clase.send_keys("txm-opgo-iwy")

#ESPERA 5 SEGUNDOS
time.sleep(5)

#APRETA EL BOTON DE UNIRSE
boton_unirse = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".VfPpkd-vQzf8d:nth-child(4)")))
boton_unirse.click()

#ESPERA 7 SEGUNDOS
time.sleep(7)

#ACEPTA LOS PERMISOS DE GOOGLE PARA EL MIC Y LA CAMARA
boton_permisos = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='yDmH0d']/div[3]/div[2]/div/div/div/div/div[2]/div/div[1]/button")))
boton_permisos.click()

#ESPERA 5 SEGUNDOS
time.sleep(5)

#PERMITIR MICROFONO Y CAMARA NOTIFICACION
permiso = WebDriverWait(driver, 10).until(EC.alert_is_present())
permiso=driver.switch_to.alert()

#DESACTIVA LA CAMARA (OPCIONAL)
camera=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "id=['yDmH0d']")))
camera.click()

#DESACTIVA EL MIC (OPCIONAL)
mic=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "id=['yDmH0d']")))
mic.click()

#SE UNE A LA CLASE
join=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "id=['yDmH0d']")))
join.click()


















   
         
