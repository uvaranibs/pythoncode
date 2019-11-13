from  selenium import webdriver
from time import sleep
driver = webdriver.Chrome(executable_path="c:\\Users\\HASAN\\Desktop\\testing\\chromedriver.exe")
driver.get("https://policytray.com")
driver.maximize_window()
print (driver.title)
driver.find_element_by_xpath("").click()
#accept alert
driver.switch_to_alert().accept()
#dismiss alert
driver.switch_to_alert().dismiss()
#send msg
driver.switch_to_alert().send_keys("hi")