from selenium import webdriver
from time import sleep
import engine

chromedriver = './chromedriver.exe'
webdriver = webdriver.Chrome(executable_path=chromedriver)

engine.init(webdriver)
engine.update(webdriver)

sleep(10)
webdriver.close()