from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\\Users\\nites\\Desktop\\crome_driver\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")
print(driver.title)
import time
time.sleep(5)
driver.quit()

