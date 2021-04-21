from selenium import webdriver
from time import sleep

driver1 = webdriver.Chrome(executable_path="chromedriver")
driver2 = webdriver.Chrome(executable_path="chromedriver")
driver3 = webdriver.Chrome(executable_path="chromedriver")

driver1.get("https://youtu.be/OCqFM1B2vdk")
driver2.get("https://youtu.be/OCqFM1B2vdk")
driver3.get("https://youtu.be/OCqFM1B2vdk")

while True:
    sleep(180)
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()

