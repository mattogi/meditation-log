import sqlite3
from sqlite3 import Error


def main():
    database = "C:/Users/Matt/PycharmProjects/MeditationLog/MeditationData.db"

    sql_create_sessions_table = """ CREATE TABLE IF NOT EXISTS sessions (
                                        id integer PRIMARY KEY autoincrement,
                                        session_begin datetime,
                                        session_end datetime,
                                        notes text
                                    ); """

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_sessions_table)

    else:
        print("Error! cannot create the database connection.")


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


if __name__ == '__main__':
    main()


