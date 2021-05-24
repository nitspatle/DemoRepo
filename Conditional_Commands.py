from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\\Users\\nites\\Desktop\\crome_driver\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
import time
time.sleep(5)
user_name=driver.find_element_by_name("txtUsername")
u_pwd=driver.find_element_by_name("txtPassword")
user_name.send_keys("Admin")
u_pwd.send_keys("admin123")
driver.find_element_by_name("Submit").click()