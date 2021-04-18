import time
import json
import os
import pygame.mixer
from scraping import Scraping
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# Initiate the browser
browser  = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
browser.maximize_window()
browser.get("https://mawaqit.net/fr/m/imam-malik-sorgues")
time.sleep(3)
os.system("xdotool key F11")
Scraping(browser)
pygame.mixer.init()
athan = pygame.mixer.Sound("athan.wav")
s = "%H:%M"
with open("horaire.json","r") as f:
    horaire = json.load(f)
while True:
    a = time.strftime(s)
    if horaire[0] == a or horaire[1] == a or horaire[2] == a or horaire[3] == a or horaire[4] == a:
        pygame.mixer.Sound.play(athan)
    if a == "00:10":
        Scraping(browser)
        with open("horaire.json","r") as f:
            horaire = json.load(f)