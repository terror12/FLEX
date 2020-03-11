from glusto.core import Glusto as g
# from flex.lib.connect.connect_to_sheets import SheetsConnector
from flex.lib.scrape.scrape_ffa import scrape_ffa
# import glob
import os
import pytest
import pyautogui
import time
from flex.utils.os_files import findNewest
from shutil import move


class TestScrape:

    g.add_log(g.log, filename='./logs/scrapelog')

    @pytest.mark.scrape_ffa
    def test_scrape_ffa(self, deftestdata, print_logging):
        """
        Download the FanDuel data for the SUN-MON slate holding all salaries.
        We will use this downloaded file in upload testing.
        :param deftestdat: Dictionary of inputs for the test
        :param print_logging: logger
        :return:
        """

        full_path_filename = deftestdata['full_path_filename']

        Scrape = scrape_ffa()

        Scrape.ffa()
        time.sleep(35)

        # start of right to the source
        pyautogui.moveTo(161, 243)
        pyautogui.click()
        time.sleep(15)
        pyautogui.moveTo(1025, 295)
        pyautogui.click()

        pyautogui.moveTo(1025, 330)
        pyautogui.click()
        time.sleep(5)

        g.log.info('Find the download file')
        FanDuel_csv = findNewest('~/Downloads')
        print(FanDuel_csv)
        dest = os.path.expanduser(full_path_filename)
        g.log.info('Check if the file already exists')
        if os.path.exists(dest):
            g.log.info('File already exists, check that you are using the right week!')
            assert False
        else:
            g.log.info('Move the Downloaded file to the correct location')
            move(FanDuel_csv, dest)
            assert True

    @pytest.mark.scrape_ffa_wo
    def test_scrape_ffa_wo_sal(self, deftestdata, print_logging):
        """
        Download the FanDuel data for the SUN-MON slate holding all salaries.
        We will use this downloaded file in upload testing.
        :param deftestdat: Dictionary of inputs for the test
        :param print_logging: logger
        :return:
        """

        # username = deftestdata['username']
        # password = deftestdata['password']
        full_path_filename = deftestdata['full_path_filename']

        Scrape = scrape_ffa()

        Scrape.ffa()
        time.sleep(35)

        pyautogui.moveTo(447, 123)
        time.sleep(30)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(477, 168)
        pyautogui.click()
        time.sleep(2)

        pyautogui.moveTo(861, 246)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(861, 276)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(1271, 691)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(875, 652)
        pyautogui.click()
        time.sleep(20)

        # start of right to the source
        pyautogui.moveTo(161, 243)
        pyautogui.click()
        time.sleep(15)
        pyautogui.moveTo(1025, 295)
        pyautogui.click()

        pyautogui.moveTo(1025, 330)
        pyautogui.click()
        time.sleep(5)

        g.log.info('Find the download file')
        FanDuel_csv = findNewest('~/Downloads')
        print(FanDuel_csv)
        dest = os.path.expanduser(full_path_filename)
        g.log.info('Check if the file already exists')
        if os.path.exists(dest):
            g.log.info('File already exists, check that you are using the right week!')
            assert False
        else:
            g.log.info('Move the Downloaded file to the correct location')
            move(FanDuel_csv, dest)
            assert True
