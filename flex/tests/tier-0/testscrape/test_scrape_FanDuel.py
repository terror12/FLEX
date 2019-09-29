from glusto.core import Glusto as g
from flex.lib.connect.connect_to_sheets import SheetsConnector
from flex.lib.scrape.selenium_FanDuel import scrape_FD
import glob
import os
import pytest
from flex.utils.os_files import findNewest
from shutil import move

class TestScrape:

    g.add_log(g.log, filename='./logs/scrapelog')

    @pytest.mark.scrape_fd
    def test_scrape_fd(self, deftestdata, print_logging):
        """

        :param rawDataframe:
        :param print_logging:
        :return:
        """

        # testdata = request.config.option.testdata[0]
        # deftestdata = read_cli(testdata)
        username = deftestdata['username']
        password = deftestdata['password']

        # Scrape = scrape_FD()
        # Scrape.FanDuel(username, password)

        FanDuel_csv = findNewest('~/Downloads')
        print(FanDuel_csv)
        dest = os.path.expanduser('~/FLEX/FLEX/flex/FanDuel_proj/')
        move(FanDuel_csv, dest)


        # my_dir = os.path.expanduser('~/Downloads')
        # def newest(path):
        #     files = os.listdir(path)
        #     paths = [os.path.join(path, basename) for basename in files]
        #     return max(paths, key=os.path.getctime)
        #
        # #with open('~/Downloads/'FanDuel-NFL', 'wb') as f:
        # list_of_files = glob.glob('~/Downloads/*.csv')  # * means all if need specific format then *.csv
        # latest_file = max(list_of_files, key=os.path.getctime)
        # print(latest_file)
        #
        # #with open('/path/I/want/to/save/file/to/file_name.pdf', 'wb') as f:
        # #    f.write(r.content)
