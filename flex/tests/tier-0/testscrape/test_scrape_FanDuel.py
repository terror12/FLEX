from glusto.core import Glusto as g
# from flex.lib.connect.connect_to_sheets import SheetsConnector
from flex.lib.scrape.selenium_FanDuel import scrape_FD
# import glob
import os
import pytest
from flex.utils.os_files import findNewest
from shutil import move


class TestScrape:

    g.add_log(g.log, filename='./logs/scrapelog')

    @pytest.mark.scrape_fd
    def test_scrape_fd(self, deftestdata, print_logging):
        """
        Download the FanDuel data for the SUN-MON slate holding all salaries.
        We will use this downloaded file in upload testing.
        :param deftestdat: Dictionary of inputs for the test
        :param print_logging: logger
        :return:
        """

        username = deftestdata['username']
        password = deftestdata['password']
        full_path_filename = deftestdata['full_path_filename']

        Scrape = scrape_FD()

        Scrape.FanDuel(username, password)

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
