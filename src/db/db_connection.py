import mysql.connector
from mysql.connector import Error
from src.utils.constants import db_password, db_user, db_host, database
from src.utils.helpers.log_setup import get_log

# getting log setup
logging = get_log()


def db_connection():
    try:
        connection = mysql.connector.connect(
            user=db_user,
            host=db_host,
            database=database,
            password=db_password
        )

        if connection.is_connected():
            logging.info('Connected to MySQL database :)')

        cursor = connection.cursor()
        return cursor, connection

    except Error as e:
        logging.error("Failed to connect to database !")
        raise e
