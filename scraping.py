from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup
import json
class Scraping():
    def __init__(self):
        horaire = self._Web_Scrap()
        self._Convertisseur(horaire)
    def _Web_Scrap(self):
        chromeOptions = Options()
        chromeOptions.headless = True
        browser  = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", options=chromeOptions)
        browser.get("https://mawaqit.net/fr/m/imam-malik-sorgues")
        sleep(25)
        soup = BeautifulSoup(browser.page_source, "html.parser")
        horaire = []
        for p in soup.find_all(class_="time"):
            horaire.append(str(p))
            browser.quit()
        return horaire
    def _Convertisseur(self,html):
        liste =[]
        for line in html:
            line = str(line)
            x = line.find('">')
            x += 2
            y = line.find("</")  
            liste.append(line[x:y].replace("<div>",""))
        with open("horaire.json","w") as f:
            json.dump(liste,f,indent=4)          

if __name__ == "__main__":
    Scraping()
