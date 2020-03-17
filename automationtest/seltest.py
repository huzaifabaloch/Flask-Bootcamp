from selenium import webdriver
from credentials import USERNAME, PASSWORD

driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('http://192.168.10.1/')

driver.find_element_by_xpath("//input[@id='username']").send_keys(USERNAME)
driver.find_element_by_xpath("//input[@id='password']").send_keys(PASSWORD)
driver.find_element_by_xpath("//input[@id='loginBtn']").click()
driver.find_element_by_xpath("//input[@value='Advanced']").click()
menu_url = driver.find_element_by_xpath("//frame[@name='menufrm']").get_attribute('src')
driver.get(menu_url)

security_window = driver.window_handles[0]

driver.find_element_by_xpath("//div[@id='folder50']/table/tbody/tr/td/a").click()

other_window = driver.window_handles[1]

driver.switch_to.window(other_window)
driver.close()

driver.switch_to.window(security_window)

mac_tab_url = driver.find_element_by_xpath("//div[@id='item53']/table/tbody/tr/td/a").get_attribute('href')

driver.get(mac_tab_url)

driver.find_element_by_xpath("//input[@value='Add']").click()
driver.implicitly_wait(2)
driver.find_element_by_xpath("//input[@name='wlFltMacAddr']").send_keys('XX:XX:XX:XX:XX')

