from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://facebook.com")
driver.maximize_window()
driver.implicitly_wait(30)

ele=driver.find_elements_by_tag_name('a')
print(len(ele))