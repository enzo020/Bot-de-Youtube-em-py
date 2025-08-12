from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()


driver.get("https://www.youtube.com")
time.sleep(3)

search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("neymar best moments")
search_box.send_keys(Keys.RETURN)
time.sleep(3)

videos = driver.find_elements(By.ID, "video-title")
videos[1].click()
time.sleep(40)
driver.quit()

#para correr o código apenas digitar 
#pythom bot.py 