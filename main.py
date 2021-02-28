import subprocess
import pyautogui
import time
import os

wd = os.getcwd()
os.chdir(r"C:\Users\stdel\OneDrive\Escritorio\BBv\plans-and-prices")
subprocess.Popen("pwd")
# os.chdir(wd)
# os.system('bash')

countries = ["bahrain","cz","dominican","algeria","guatemala","botswana","botswana","kuwait","cote","cote",
            "madagascar","madagascar","namibia","namibia","palestine","palestine","palestine",
            "chad","chad","chad","chad","chad","tunisia","tunisia","tunisia","tunisia","tunisia","tunisia",
            "nigieria","peru","paraguay","turkey"]

isocode_countries = ["BH","CZ","DO","DZ","GT","BW","BW","KW","CI","CI","MG","MG","NA","NA","PS","PS","PS",
                    "TD","TD","TD","TD","TD","TN","TN","TN","TN","TN","TN","NG","PE","PY","TR"]

platforms = ["Crunchyroll","YoutubePremium","Crunchyroll","Crunchyroll","Crunchyroll","Iroko","AmazonPrime",
            "AmazonPrime","AmazonPrime","Iroko","AmazonPrime","Iroko","AmazonPrime","Iroko","Osn","StarzPlay",
            "Weyyak","AmazonPrime","Iroko","Osn","ShahidPlus","StarzPlay","Osn","ShahidPlus","AmazonPrime","ErosNow",
            "StarzPlay","Crunchyroll","Crunchyroll","Crunchyroll","Crunchyroll","YoutubePremium"]

def cambiarPaisVPN(pais):
    pyautogui.click(172,750)
    time.sleep(1)
    pyautogui.click(665, 545)
    time.sleep(1)
    pyautogui.typewrite(pais)
    time.sleep(1)
    pyautogui.click(600, 285)
    time.sleep(20)
    pyautogui.click(172,750)

if __name__ == "__main__":

    if len(countries) == len(isocode_countries) and len(countries) == len(platforms):
        ultimo_pais = ''
        for i in range(len(countries)):
            if ultimo_pais != countries[i]:
                cambiarPaisVPN(countries[i])
                subprocess.call("python main.py --c {isocode} --o scraping {platform}{isocode}".format(isocode=isocode_countries[i], platform=platforms[i]), shell=True)
                ultimo_pais = countries[i]
            else:
                subprocess.call("python main.py --c {isocode} --o scraping {platform}{isocode}".format(isocode=isocode_countries[i], platform=platforms[i]), shell=True)
                ultimo_pais = countries[i]
    else:
        print('El tamaño de los arrays son diferentes')

    