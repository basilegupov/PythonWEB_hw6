from sqlite3 import Error

from connect import create_connection, read_sql_file


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


if __name__ == '__main__':
    sql_create_tables = read_sql_file('create_tables.sql')

    with create_connection() as conn:
        if conn is not None:
            create_table(conn, sql_create_tables)
        else:
            print("Error! cannot create the database connection.")
