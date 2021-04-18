from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from bs4 import BeautifulSoup
import json
class Scraping():
    def __init__(self,browser):
        horaire = self._Web_Scrap(browser)
        self._Convertisseur(horaire)
    def _Web_Scrap(self,browser):
        # Initiate the browser
        #browser  = webdriver.Chrome(ChromeDriverManager().install())
        #browser.maximize_window()
        #browser.get("https://mawaqit.net/fr/m/imam-malik-sorgues")
        #sleep(3)
        browser.find_element_by_id("cookie-accept-button").click()
        soup = BeautifulSoup(browser.page_source, "html.parser")
        horaire = []
        for p in soup.find_all(class_="time"):
            horaire.append(str(p))
        return horaire
    def _Convertisseur(self,html):
        liste =[]
        for line in html:
            line = str(line)
            x = line.find('">')
            x += 2
            y = line.find("</")  
            liste.append(line[x:y])
        with open("horaire.json","w") as f:
            json.dump(liste,f,indent=4)          

if __name__ == "__main__":
    Scraping()