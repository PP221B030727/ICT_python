from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#Fin the research bar and write in it

#Create your browser
browser = webdriver.Firefox()  
#open the required page
browser.get("https://www.python.org")
browser.maximize_window()


search_bar = browser.find_element(By.NAME, "q")
search_bar.clear()
search_bar.send_keys("getting started with python")
