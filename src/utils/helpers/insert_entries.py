import pandas as pd
from src.db.db_connection import db_connection
from src.utils.constants import campaign_data, table_name
from src.utils.helpers.log_setup import get_log

# getting log setup
logging = get_log()


def insert_data_into_mysql(csv_file, db_config, table):
    """
    Function to read csv file and insert the entries from that file to mysql database table.
    @param csv_file:
    @param db_config:
    @param table:
    @return: response message
    """
    try:
        logging.info("Read the CSV file into a pandas DataFrame and insert entries to database")
        logging.debug(f"Reading csv file from: {campaign_data}")
        df = pd.read_csv(csv_file)

        logging.debug(f"Dropping index column from dataframe file from: {campaign_data}")
        df = df.drop("Index", axis=1)

        logging.info("Establish a connection to the MySQL server")
        cursor, connection = db_config

        logging.debug("Getting columns from dataframe")
        columns = ", ".join(df.columns)

        logging.debug("Converting columns name to lower case")
        columns = columns.lower()

        query_template = f"INSERT INTO sadd ({columns}) VALUES ({', '.join(['%s'] * len(df.columns))})"

        data = [tuple(row) for row in df.itertuples(index=False)]

        logging.info("Insert data into the MySQL table using executemany")
        logging.debug("Executing query for inserting entries")
        cursor.executemany(query_template, data)

        logging.info("Commit the changes and close the cursor and connection")

        logging.debug("Committing the changes to the database")
        connection.commit()

        logging.debug("Closing the cursor")
        cursor.close()

        logging.debug("Closing the connection")
        connection.close()

        logging.info(f"Task: Data inserted successfully into table: {table}!")

    except Exception as e:
        logging.error(f"Some error occurred in inserting entries into database !, Error: {e}")

    finally:
        try:
            if cursor:
                cursor.close()
                logging.info("Task: Mysql cursor closed")

        except Exception as e:
            logging.error(f"Some error occurred in closing cursor, Error: {e}")

        try:
            if connection and connection.is_connected():
                connection.close()
                logging.info("Task: Mysql connection closed")

        except Exception as e:
            logging.error(f"Some error occurred in closing connection, Error: {e}")


"""comment out this below line to use this code for inserting entries"""
# insert_data_into_mysql(campaign_data, db_connection(), table_name)
