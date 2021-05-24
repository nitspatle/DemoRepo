from selenium import webdriver
from selenium.webdriver.common.keys import Keys
DRIVER_PATH="C:\\Users\\nites\\Desktop\\crome_driver\\chromedriver.exe"
URL_PATH="https://opensource-demo.orangehrmlive.com/"
driver=webdriver.Chrome(DRIVER_PATH)
driver.get(URL_PATH)
import time
time.sleep(5)
#Remaining to implement to implicit wait & explicit wait
