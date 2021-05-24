from select import select
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome(executable_path="C:\\Users\\nites\\Desktop\\crome_driver\\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
ele=driver.find_element_by_id("RESULT_RadioButton-9")
ele_select=Select(ele)
ele_select.select_by_index(1)
time.sleep(5)
ele_select.select_by_value("Radio-1")
time.sleep(4)
ele_select.select_by_visible_text("Morning")
time.sleep(4)
print(len(ele_select.options))
all_option=ele_select.options
for elemen in all_option:
   print(elemen.text)
time.sleep(4)
driver.close()