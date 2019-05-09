
from apiclient import discovery
import httplib2
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import os
import pandas as pd

class GoogleSheetsConnector():
    """
    Class object to hold credentials for connecting to google sheets
    """

    def __init__(self, spreadsheetId, rangeName):
        self.credentials = self.get_credentials()
        self.spreadsheetId = spreadsheetId
        self.rangeName = rangeName


    def get_credentials(self):
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'sheets.googleapis.com-python-quickstart.json')
        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else:  # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials


    def rd_sheet(self):
        """
        Method to read from GoogleSheets using credentials object from 'get_credentials()'
        :return result: Object holding values from the Googlesheet, among other things I assume be we are only using 'values'
        """

        http = self.credentials.authorize(httplib2.Http())
        discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                        'version=v4')
        service = discovery.build('sheets', 'v4', http=http,
                                  discoveryServiceUrl=discoveryUrl)
        result = service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheetId, range=self.rangeName).execute()

        return result


    def result_to_df(self):
        """
        Turns Googlesheet result data into DataFrame and separates just the values
        :return full_df: Dataframe holding everything in Goooglsheet
        """

        full_df = pd.DataFrame(self.rd_sheet()['values'])

        return full_df


# Instantiate Class object
FLEX = GoogleSheetsConnector('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537')

# Start using methods
FLEX.get_credentials()
FLEX.rd_sheet()
FLEX.result_to_df()