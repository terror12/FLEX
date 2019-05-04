
from flex.lib.connect.connect_to_sheets import GoogleSheetsConnector as gsc

test_credentials():
    gsc = gsc()
    assert gsc