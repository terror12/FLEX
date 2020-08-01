import psycopg2


class UpdateDB:

    def get_connection(self, dbname, user, password):
        connection = psycopg2.connect(f"dbname={dbname} user={user} password={password}")
        return connection

    def fetch_table_data(self, connection, tablename):
        cursor = connection.cursor()
        postgreSQL_select_Query = f"select * from {tablename}"
        cursor.execute(postgreSQL_select_Query)
        lineup = cursor.fetchall()

        print("lineup is")
        print(lineup)
        return lineup

    def update_table_data(self, connection, player, team, salary,  position, projection, std, tablename, count):
        cursor = connection.cursor()
        pg_update = f"update {tablename} set player = '{player}', team = '{team}', salary = '{salary}', position = '{position}', projection = '{projection}', std = '{std}' where id = {count}"  # noqa E501
        cursor.execute(pg_update)
        connection.commit()
