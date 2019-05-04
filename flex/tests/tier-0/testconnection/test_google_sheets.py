from glusto.core import Glusto as g
from flex.lib.connect.connect_to_sheets import GoogleSheetsConnector

def test_credentials():
    """
    Assert that we have a credentials object
    :return:
    """
    g.add_log(g.log, filename='STDOUT')
    g.add_log(g.log, filename='./Googleconnectorlog')

    gsc = GoogleSheetsConnector()
    g.log.info(gsc.get_credentials())
    assert gsc.get_credentials()

def test_read_sheet():
    """
    Test that we can read a sheet using the credential object
    :return:
    """
    gsc = GoogleSheetsConnector()
#    credentials = gsc.get_credentials()
    g.log.info(gsc.get_credentials())
    full_df = gsc.posDframe('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537')
    g.log.info(full_df)
    assert 'FanDuel_Salary' in full_df