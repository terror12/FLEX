from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
option.add_argument(" — incognito")
option.add_argument("--start-maximized")

browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=option)

browser.get("https://www.fanduel.com/contests/nfl/3036")


print(browser)




inputElement = browser.find_element_by_id("forms.login.email")
inputElement.send_keys('REDACTED')

inputElement = browser.find_element_by_id("forms.login.password")
inputElement.send_keys('REDACTED')

inputElement.send_keys(Keys.ENTER)

time.sleep(1.9)

browser.find_element_by_xpath("//span[contains(text(), 'SUN-MON')]").click()
print('#0')

print(browser)
browser.find_element_by_xpath("//div[contains(@class, '_a _b _c _d _e _f _g')]") #.click()
print(browser)
browser.find_element_by_xpath("//div[contains(@class, 'ReactVirtualized__Grid__innerScrollContainer')]").click()
element = browser.find_element_by_xpath("//iframe[@class='zEWidget-launcher zEWidget-launcher--active']")
browser.execute_script("arguments[0].style.visibility='hidden'", element)

browser.find_element_by_xpath("//a[contains(@class, 'contest_details__enter_link')]").click()
browser.find_element_by_xpath("//a[contains(@class, 'button tiny text download-players')]").click()
time.sleep(15)

browser.quit()
