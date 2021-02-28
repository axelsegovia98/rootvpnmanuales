import subprocess
import pyautogui
import time
import os
import json
import all_countries


fix_platforms = []

paises = all_countries.all_countries
json_path = r'.\rootPreciosHMA.json'

with open(json_path, 'r') as file:
    json_file = json.load(file)
    
wd = os.getcwd()
os.chdir(r"C:\Users\axels\Documents\GitHub\plans-and-prices")


def cambiarPaisVPN(pais):
    pyautogui.click(31,335)
    time.sleep(1)
    pyautogui.click(947, 713)
    time.sleep(1)
    pyautogui.typewrite(pais)
    time.sleep(1)
    pyautogui.click(950, 458)
    time.sleep(20)
    pyautogui.click(31,335)


if __name__ == "__main__":
    for countries in json_file:
        for data in countries:
            cambiarPaisVPN(paises[data])
            for platform in countries[data]:
                try:
                    subprocess.call("python main.py --c {isocode} --o scraping {platform}".format(isocode=platform['Country'], platform=platform['PlatformCode']), shell=True)