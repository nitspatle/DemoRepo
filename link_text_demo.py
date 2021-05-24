from selenium import webdriver
#from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\\Users\\nites\\Desktop\\crome_driver\\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
link_a=driver.find_element_by_tag_name("a")
print(len(link_a))
time.sleep(5)
driver.close()