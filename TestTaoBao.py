from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

driver = webdriver.Firefox()
base_url = "https://world.taobao.com/"
verificationErrors = []
accept_next_alert = True
driver.get(base_url + "/search/search.htm?sort=_deal&_ksTS=1491487495190_753&spm=a21bp.7806943.20151106.1&style=list&json=on&cna=6CuTDXxTCQMCAXvBeoqWnPRj&module=sortList&_input_charset=utf-8&navigator=all&s=0&q=%E8%80%81%E4%BA%BA&callback=__jsonp_cb&abtest=_AB-LR517-LR854-LR895-PR517-PR854-PR895")
#driver.find_element_by_css_selector("button.btn-search.seahd-iconfont").click()
# ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=nameStorage:_e_0gll?wm_referrer=https%3A%2F%2Fworld.taobao.com%2Fsearch%2Fsearch.htm%3Fsort%3D_deal%26_ksTS%3D1491487495190_753%26spm%3Da21bp.7806943.20151106.1%26style%3Dlist%26json%3Don%26cna%3D6CuTDXxTCQMCAXvBeoqWnPRj%26module%3DsortList%26_input_charset%3Dutf-8%26navigator%3Dall%26s%3D0%26q%3D%25E8%2580%2581%25E4%25BA%25BA%26callback%3D__jsonp_cb%26abtest%3D_AB-LR517-LR854-LR895-PR517-PR854-PR895&refer_pv_id=tHlzc6 | ]]
#driver.find_element_by_css_selector("span.icon.icon-list").click()
elements = driver.find_elements_by_class_name("J_AtpLog")
for element in elements:
 print element.text
# ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=nameStorage:_e_0gll?wm_referrer=https%3A%2F%2Fworld.taobao.com%2Fsearch%2Fsearch.htm%3Fsort%3D_deal%26_ksTS%3D1491487495190_753%26spm%3Da21bp.7806943.20151106.1%26style%3Dlist%26json%3Don%26cna%3D6CuTDXxTCQMCAXvBeoqWnPRj%26module%3DsortList%26_input_charset%3Dutf-8%26navigator%3Dall%26s%3D0%26q%3D%25E8%2580%2581%25E4%25BA%25BA%26callback%3D__jsonp_cb%26abtest%3D_AB-LR517-LR854-LR895-PR517-PR854-PR895&refer_pv_id=tHlzc6 | ]]
time.sleep(2)
driver.find_element_by_link_text("2").click();
time.sleep(2)