import psycopg2


class UpdateDB:

    def get_connection(self, dbname, user, password, host):
        connection = psycopg2.connect(f"dbname={dbname} user={user} password={password} host={host} sslmode=require")
        return connection

    def create_table(self, connection, tablename):
        """ create tables in the PostgreSQL database"""
        try:
            cursor = connection.cursor()
            postgreSQL_create_table = f"create table {tablename} (id serial PRIMARY KEY, num integer, data varchar);"
            cursor.execute(postgreSQL_create_table)
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def fetch_table_data(self, connection, tablename):
        cursor = connection.cursor()
        postgreSQL_select_Query = f"select * from {tablename}"
        cursor.execute(postgreSQL_select_Query)
        lineup = cursor.fetchall()

        print("lineup is")
        print(lineup)
        return lineup

    def update_table_data(self, connection, player, team, salary, position, projection, std, tablename, count, row):
        cursor = connection.cursor()
        pg_update = f"update {tablename} set player = '{player}', team = '{team}', salary = '{salary}', position = '{position}', projection = '{projection}', std = '{std}' where id = {row}"  # noqa E501
        cursor.execute(pg_update)
        connection.commit()

    def insert_table_data(self, connection, df, tablename):
        df.to_sql(tablename, connection, if_exists='replace')
        # pg_insert = f"insert into {tablename} values player = '{player}', team = '{team}', salary = '{salary}', position = '{position}', projection = '{projection}', std = '{std}' where id = {row}"  # noqa E501
        # cursor.execute(pg_insert)
        connection.commit()

    def delete_table(self, connection, tablename):
        """ deletes tables in the PostgreSQL database"""
        try:
            cursor = connection.cursor()
            postgreSQL_delete_table = f"DROP TABLE IF EXISTS {tablename};"
            cursor.execute(postgreSQL_delete_table)
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
