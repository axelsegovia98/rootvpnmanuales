import subprocess
import pyautogui
import time
import os
import json
import argparse
import all_countries #Diccionario que contiene el ISOCODE como /clave/ y el nombre del país como /valor/

paises = all_countries.all_countries #Se pone en una variable el diccionario dentro de all_countries.py (quizás se puede hacer de una mejor manera)


def cambiarPaisVPN(pais, developer):
    #pyautogui.position() #Para ir viendo en que posición está el mouse
    
    coordenadas_santiago = ((172,750), (665, 545), (600, 285), (172,750))
    coordenadas_axel     = ((31,335), (947, 713), (950, 458), (31,335))

    if developer == 'santiago':
        coordenadas = coordenadas_santiago
    if developer == 'axel':
        coordenadas = coordenadas_axel
    
    #Se clickea HMA en la barra de tareas. Tiene que estar abajo del ícono de WSP (en mi caso)
    pyautogui.click(coordenadas[0])
    time.sleep(1)
    #Se clickea el botón de los países
    pyautogui.click(coordenadas[1])
    time.sleep(1)
    pyautogui.typewrite(pais)
    time.sleep(1)
    #Se clickea el pais
    pyautogui.click(coordenadas[2])
    time.sleep(20)
    #Se clickea HMA en la barra de tareas. Tiene que estar abajo del ícono de WSP (en mi caso)
    pyautogui.click(coordenadas[3])


if __name__ == "__main__": #Santi ayudame no sé para que sirve esto pero sirve x2
    parser =  argparse.ArgumentParser()
    parser.add_argument('--d',        help = 'Developer', type = str)
    
    args = parser.parse_args()
    developer = args.d
    
    json_path = r'.\rootPreciosHMA.json' #Se guarda la ruta del json que contiene la información de las plataformas a ejecutarse 
    with open(json_path, 'r') as file: #Se abre y se guarda el json en la variable json_file
        json_file = json.load(file)
    
    if developer == 'santiago':
        wd = os.getcwd()
        os.chdir(r"C:\Users\stdel\OneDrive\Escritorio\BBv\plans-and-prices")
        subprocess.Popen("pwd")
        
    if developer == 'axel':
        wd = os.getcwd() #Santi ayudame no sé para que sirve esto pero sirve
        os.chdir(r"C:\Users\axels\Documents\GitHub\plans-and-prices") #Ruta que contiene al proyecto
        subprocess.call(r"env\scripts\activate", shell=True) #Se supone que con esto me evito activar el env, pero me equivoque un día y me instalé todas las bibliotecas sin usar el env así que no se si funciona

        
    for countries in json_file: #En este punto de json se ven las plataformas en general
        for data in countries: #En este punto del json se guarda el ISOCODE que identifica a cada agrupación de objetos por país
            cambiarPaisVPN(paises[data], developer) #Se usa el diccionario usando de clave el valor del ISOCODE
            for platform in countries[data]: #Se recorre cada plataforma dentro de cada agrupación de objetos por pais
                try:
                    #Se ejecuta la plataforma
                    subprocess.call("python main.py --c {isocode} --o scraping {platform}".format(isocode=platform['Country'], platform=platform['PlatformCode']), shell=True)
                except Exception as error:
                    #Acá veo como va explotando todo el código si me equivoco xd
                    print('Error de ejecución: ', error)