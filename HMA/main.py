import subprocess
import pyautogui
import time
import os
import json
import all_countries #Diccionario que contiene el ISOCODE como /clave/ y el nombre del país como /valor/

fix_platforms = []

paises = all_countries.all_countries #Se pone en una variable el diccionario dentro de all_countries.py (quizás se puede hacer de una mejor manera)
json_path = r'.\rootPreciosHMA.json' #Se guarda la ruta del json que contiene la información de las plataformas a ejecutarse 

with open(json_path, 'r') as file: #Se abre y se guarda el json en la variable json_file
    json_file = json.load(file)
    
wd = os.getcwd() #Santi ayudame no sé para que sirve esto pero sirve
os.chdir(r"C:\Users\axels\Documents\GitHub\plans-and-prices") #Ruta que contiene al proyecto
subprocess.call(r"env\scripts\activate", shell=True) #Se supone que con esto me evito activar el env, pero me equivoque un día y me instalé todas las bibliotecas sin usar el env


def cambiarPaisVPN(pais):
    
    #pyautogui.position() #Para ir viendo en que posición está el mouse
    
    #Se clickea HMA en la barra de tareas. Tiene que estar abajo del ícono de WSP (en mi caso)
    pyautogui.click(31,335)
    time.sleep(1)
    #Se clickea el botón de los países
    pyautogui.click(947, 713)
    time.sleep(1)
    pyautogui.typewrite(pais)
    time.sleep(1)
    #Se clickea el pais
    pyautogui.click(950, 458)
    time.sleep(20)
    #Se clickea HMA en la barra de tareas. Tiene que estar abajo del ícono de WSP (en mi caso)
    pyautogui.click(31,335)


if __name__ == "__main__": #Santi ayudame no sé para que sirve esto pero sirve x2
    
    for countries in json_file: #En este punto de json se ven las plataformas en general
        for data in countries: #En este punto del json se guarda el ISOCODE que identifica a cada agrupación de objetos por país
            cambiarPaisVPN(paises[data]) #Se usa el diccionario usando de clave el valor del ISOCODE
            for platform in countries[data]: #Se recorre cada plataforma dentro de cada agrupación de objetos por pais
                try:
                    #Se ejecuta la plataforma y la idea de asignarlo a una variable es para agarrar el return, COSA QUE NO LO HACE
                    exec_platform = subprocess.call("python main.py --c {isocode} --o scraping {platform}".format(isocode=platform['Country'], platform=platform['PlatformCode']), shell=True)
                    
                    #Se intenta crear un array que tenga el nombre de la plataforma y el valor que trae el return
                    error_log = {platform['PlatformCode'], exec_platform}
                    #Se agrega el log a fix_platforms
                    fix_platforms.append(error_log)
                    
                except Exception as error:
                    #Acá veo como va explotando todo el código si me equivoco xd
                    print('pasó al except: ', error)
    
    for error in fix_platforms:
        #Para ver que cosas se guardan en fix_platforms
        print(error)
    
    #Como me da ansiedad de que no imprima bien las cosas, imprimo el array completo
    print(fix_platforms)