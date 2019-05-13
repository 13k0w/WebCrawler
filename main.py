from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
# options.add_argument("--headless")
browser = webdriver.Firefox(firefox_options=options)

browser.get("https://www.google.com")
browser.quit()
