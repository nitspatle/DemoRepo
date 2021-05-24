import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\\Users\\nites\\Desktop\\crome_driver\\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
radio_button_name_male=driver.find_element_by_xpath("//*[@id='q26']/table/tbody/tr[1]/td/label").click()
time.sleep(5)
radio_button_name_female=driver.find_element_by_xpath("//*[@id='q26']/table/tbody/tr[2]/td/label").click()
time.sleep(5)
checkbox_button_monday=driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[2]/td/label").click()
time.sleep(5)
submit_button_click=driver.find_element_by_name("Submit").click()
time.sleep(5)
driver.close()
