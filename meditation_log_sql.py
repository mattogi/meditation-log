import sqlite3
from sqlite3 import Error


class MeditationLogSQL:
    def __init__(self, database):
        self.database = database

    def create_connection(self):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        try:
            conn = sqlite3.connect(self.database)
            return conn
        except Error as e:
            print(e)

        return None

    def insert_session(self, session_values):
        connect = self.create_connection()
        c = connect.cursor()

        sql_insert_session = """ INSERT INTO sessions(session_begin, session_end, notes)
                                 VALUES(?,?,?) """

        c.execute(sql_insert_session, session_values)

        connect.commit()
        connect.close()

    def update_session(self):
        pass
        connect = self.create_connection()
        c = connect.cursor()

        sql_update_session = ""

        c.execute(sql_update_session)

        connect.commit()
        connect.close()

    def delete_session(self):
        pass
        connect = self.create_connection()
        c = connect.cursor()

        sql_delete_session = ""

        c.execute(sql_delete_session)

        connect.commit()
        connect.close()

    def get_session(self, session_id):
        connect = self.create_connection()
        c = connect.cursor()

        sql_get_session = "select * from sessions"

        c.execute(sql_get_session)

        session = c.fetchone()

        connect.close()

        return session
