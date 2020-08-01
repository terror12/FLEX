from glusto.core import Glusto as g
from flex.lib.postgresql_database.update_database import UpdateDB
import pandas as pd
import pytest


class TestUpdateDatabase:
    g.add_log(g.log, filename='./logs/UpdateDatabaseLog')

    @pytest.mark.db_conn
    def test_database_connection(self, deftestdata, print_logging):
        """
        This test will make a connection my postgresql database.
        :return:
        """

        dbname = deftestdata['dbname']
        user = deftestdata['user']
        password = deftestdata['password']

        g.log.info('Instantiate UpdateDB class')
        updatedb = UpdateDB()
        g.log.info('Test for connection')
        connection = updatedb.get_connection(dbname, user, password)
        cursor = connection.cursor()
        if cursor:
            g.log.info('Connection to Database was successful')
        else:
            pytest.fail('Connection to Database failed')

    @pytest.mark.fetch_table_data
    def test_fetch_table_data(self, deftestdata, print_logging):
        """
        This test will make a connection my postgresql database and fetch what exists
        :return:
        """

        dbname = deftestdata['dbname']
        user = deftestdata['user']
        password = deftestdata['password']
        tablename = deftestdata['tablename']

        g.log.info('Instantiate UpdateDB class')
        updatedb = UpdateDB()

        g.log.info('get connection')
        connection = updatedb.get_connection(dbname, user, password)

        g.log.info('Fetch table data')
        lineup = updatedb.fetch_table_data(connection, tablename)

        if lineup:
            g.log.info('table fetch returned an object')
        else:
            pytest.fail('Table fetch failed')

    @pytest.mark.update_db
    def test_update_db(self, deftestdata, print_logging):
        """
        This test will make a connection my postgresql database, fetch what exists
        update existing data and save changes to database.
        :return:
        """

        dbname = deftestdata['dbname']
        user = deftestdata['user']
        password = deftestdata['password']
        tablename = deftestdata['tablename']
        result = deftestdata['result']

        g.log.info('Instantiate UpdateDB class')
        updatedb = UpdateDB()

        g.log.info('get connection')
        connection = updatedb.get_connection(dbname, user, password)

        g.log.info('Fetch table data')
        lineup = updatedb.fetch_table_data(connection, tablename)

        df = pd.read_csv(result)
        count = 0
        for i in lineup:
            count += 1
            player = df.iloc[count-1].Player
            team = df.iloc[count-1].Team
            salary = df.iloc[count-1].Salary
            position = df.iloc[count-1].Position
            projection = df.iloc[count-1].Projection
            std = df.iloc[count-1].STD
            updatedb.update_table_data(connection, player, team, salary, position, projection, std, tablename, count)
            # cursor = connection.cursor()
            # pg_update = f"Update ffautoduel_data set player = '{df.iloc[count-1].Player}' where id = {count}"
            # cursor.execute(pg_update)

        lineup = updatedb.fetch_table_data(connection, tablename)
        print(lineup[count-1])
        if df.iloc[count-1].Player in lineup[count-1]:
            g.log.info('table update worked')
        else:
            pytest.fail('Table update failed')
