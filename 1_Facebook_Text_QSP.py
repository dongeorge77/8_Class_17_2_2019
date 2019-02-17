from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://facebook.com")
driver.maximize_window()
driver.implicitly_wait(30)

ele=driver.find_elements_by_xpath("//input[@type='email' or @type='password' or @id='u_0_j' or @id='u_0_1' or @type='text']")
for data in ele:
    data.send_keys('QSpiders')