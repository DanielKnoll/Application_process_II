from db_config import Config
import psycopg2
import psycopg2.extras


def open_database():
    try:
        connection_string = Config.DB_CONNECTION_STR
        connection = psycopg2.connect(connection_string)
        connection.autocommit = True
    except psycopg2.DatabaseError as exception:
        print(exception)
    return connection


def connection_handler(function):
    def wrapper(*args, **kwargs):
        ret_value = ""
        connection = open_database()
        dict_cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = function(*args, **kwargs)
        if args and args[0] == "Do not fetch":
            dict_cur.execute(query)
        else:    
            dict_cur.execute(query)
            ret_value = dict_cur.fetchall()
        dict_cur.close()
        connection.close()
        return ret_value
    return wrapper
