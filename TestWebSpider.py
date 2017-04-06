from selenium import webdriver
driver=webdriver.Ie()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("Selenium2")
driver.find_element_by_id("su").click()
#driver.quit()