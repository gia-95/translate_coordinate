from selenium import webdriver #auto
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.action_chains import ActionChains

# pip install selenium


## READ FROM FILE ##

## Variabili
address_list = []
address_coord = {}

## Leggi indirizzi da file txt
file = open('indirizzi.txt','r')
file_content = file.read()
file.close()

# Sistema le stringhe lette
address_list_temp = file_content.split('/')
for address in address_list_temp :
    address_list.append(address.strip())

time.sleep(1)
print("\nIndirizzi trovati nel file:", len(address_list))
time.sleep(1)



### DRIVER FIREFOX ###

print("\n# Start driver Selenium (Firefox)...")
    
# Firefox Options
options = FirefoxOptions()
# options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

## Istruzioni...
driver.get("https://www.gps-longitudine-latitudine.it/")
time.sleep(3) 

# btn 'Acconsento'
driver.find_element(By.XPATH, "//p[./text()=\'Consent\']/parent::*").click()
time.sleep(1)

# btn 'x - cookie'
driver.find_element(By.XPATH, "//img[@class='zuzcookiex']").click()
time.sleep(1)


# input - searchterm
search_address_input = driver.find_element(By.XPATH, "//input[@id='searchterm']")

for address in address_list : 

    search_address_input.clear() # Pulisci campo input

    search_address_input.send_keys(address) # scrivi address in input

    driver.find_element(By.XPATH, "//div[@class='btn']").click() # Click 'Trova!'
    time.sleep(1)

    coordinateHTML = driver.find_element(By.XPATH, "//span[@class='coordinates']/parent::p/following-sibling::p/span")
    coordinate_string  = coordinateHTML.get_attribute("innerHTML")
    print(address, "->", coordinate_string)

    time.sleep(1)

    lat = coordinate_string.split(',')[0][1:]
    lng = coordinate_string.split(',')[1][1:-1]

    with open('indirizzi_coord.txt', 'a') as f:
        f.write('{\n')
        f.write(f'  indirizzo: \'{address}\'\n')
        f.write(f'  lat: {lat}\n')
        f.write(f'  lng: {lng}\n')
        f.write('},\n')



time.sleep(1)
driver.close()


