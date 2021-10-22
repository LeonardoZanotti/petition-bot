#!/usr/bin/env python3
# Leonardo José Zanotti
# https://github.com/LeonardoZanotti/petition-bot

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://google.com')
print(driver.title)
driver.quit()
