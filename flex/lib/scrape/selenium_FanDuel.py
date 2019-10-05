from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from retrying import retry

class scrape_FD():
    """
    Class to hold functions needed to create a valid lineup.
    """
    # TODO: create __init__ method to instantiate assemble object
    @retry
    def FanDuel(self, username, password):

        option = webdriver.ChromeOptions()
        option.add_argument(" — incognito")
        option.add_argument("--start-maximized")
        browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=option)
        browser.get("https://www.fanduel.com/contests/nfl/3036")
        print(browser)
        # Login to FanDuel
        inputElement = browser.find_element_by_id("forms.login.email")
        inputElement.send_keys(username)
        inputElement = browser.find_element_by_id("forms.login.password")
        inputElement.send_keys(password)
        inputElement.send_keys(Keys.ENTER)
        # This timed sleep can be finicky. It needs to wait a second for the page to come up and make the element
        # available but if it waits too long a pop up appears and blocks the element
        time.sleep(1.9)
        # Select teh SUN-MON slate
        browser.find_element_by_xpath("//span[contains(text(), 'SUN-MON')]").click()
        print(browser)
        # Select a lobby
        time.sleep(2)
        browser.find_element_by_xpath("//div[contains(@class, '_a _b _c _d _e _f _g')]")
        browser.find_element_by_xpath("//div[contains(@class, 'ReactVirtualized__Grid__innerScrollContainer')]").click()
        # Remove the Customer service pop up widget
        element = browser.find_element_by_xpath("//iframe[@class='zEWidget-launcher zEWidget-launcher--active']")
        browser.execute_script("arguments[0].style.visibility='hidden'", element)
        # Click enter a lineup
        browser.find_element_by_xpath("//a[contains(@class, 'contest_details__enter_link')]").click()
        # All of this brings us to the point where we can select the download-players button.
        browser.find_element_by_xpath("//a[contains(@class, 'button tiny text download-players')]").click()
        time.sleep(5)
        # Close Window.
        browser.quit()