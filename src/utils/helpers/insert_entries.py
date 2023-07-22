import pandas as pd
from src.db.db_connection import db_connection
from src.utils.constants import campaign_data, table_name
from src.utils.helpers.log_setup import get_log

# getting log setup
logging = get_log()


def insert_data_into_mysql(csv_file, db_config, table):
    try:
        logging.info("Read the CSV file into a pandas DataFrame")
        df = pd.read_csv(csv_file)

        logging.info("Establish a connection to the MySQL server")
        cursor, connection = db_config

        logging.info("Getting columns from dataframe")
        columns = ", ".join(df.columns)

        query_template = f"INSERT INTO {table} ({columns}) VALUES ({', '.join(['%s'] * len(df.columns))})"

        data = [tuple(row) for row in df.itertuples(index=False)]

        logging.info("Insert data into the MySQL table using executemany")
        cursor.executemany(query_template, data)

        logging.info("Commit the changes and close the cursor and connection")
        connection.commit()
        cursor.close()
        connection.close()

        print("Data inserted successfully!")

    except Exception as e:
        print(f"Error: {e}")

# insert_data_into_mysql(campaign_data, db_connection(), table_name)
