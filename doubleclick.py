from selenium import webdriver
import time
from selenium.webdriver import ActionChains
driver = webdriver.Chrome(executable_path="c:\\Users\\HASAN\\Desktop\\testing\\chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")
print (driver.title)
driver.maximize_window()
copy_text=driver.find_element_by_xpath("//button[text()='Copy Text']")
actions=ActionChains(driver)
actions.double_click(copy_text).perform()
#right click
#button=driver.find_element_by_xpath("")
#actions=ActionChains(driver)
#actions.context_click(button).perform()
bjhvjgvhchc
