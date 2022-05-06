from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://zefoy.com/")
browser.add_cookie({"name": "PHPSESSID", "value": "403eo1cmnlrojai9d6u445e4q1"})
browser.refresh()
time.sleep(30)