from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()  
#open the required page
browser.get("https://www.python.org")
browser.maximize_window()
print(browser.title)
