from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\\Users\\nites\\Desktop\\crome_driver\\chromedriver.exe")
driver.get("https://demoqa.com/text-box")
import time
full_name=driver.find_element_by_id("userName").send_keys("Nitesh Hemraj Patle")
time.sleep(5)
gmail_name=driver.find_element_by_id("userEmail").send_keys("niteshpatle118@gmail.com")
time.sleep(5)
current_address_name=driver.find_element_by_id("currentAddress").send_keys("At hiratola")
time.sleep(5)
permanet_add_name=driver.find_element_by_id("permanentAddress").send_keys("At hiratola")
time.sleep(5)

button_submit=driver.find_element_by_id("submit").click()
time.sleep(5)
driver.close()
