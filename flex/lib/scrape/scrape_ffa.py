from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from retrying import retry
import webbrowser

class scrape_ffa():
    """
    Class to hold functions needed to create a valid lineup.
    """
    # TODO: create __init__ method to instantiate assemble object
    def ffa(self):

        a_website = "https://apps.fantasyfootballanalytics.net"

        # Open url in a new window of the default browser, if possible
        webbrowser.open_new(a_website)
