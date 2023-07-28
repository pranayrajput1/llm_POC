import mysql.connector
from mysql.connector import Error
from src.utils.constants import db_password, db_user, db_host, database

# getting log setup


def db_connection():
    try:
        connection = mysql.connector.connect(
            user=db_user,
            host=db_host,
            database=database,
            password=db_password
        )

        if connection.is_connected():
            cursor = connection.cursor()
        return cursor, connection

    except Error as e:
        raise e
