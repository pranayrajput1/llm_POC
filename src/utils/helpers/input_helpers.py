from src.db.db_connection import db_connection
from src.utils.constants import table_name, action_list, platform_list
import logging


# getting log setup

def get_log():
    """
    Initializing logger basic configuration
    """
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    return logging


def get_user_query():
    query_input = input("Enter your query: ")
    return query_input


def run_query(query):
    # logging.info("Task: Connecting with database")
    cursor, conn = db_connection()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data


def convert_list_items_to_lowercase(input_list):
    return [item.lower() for item in input_list]


def validate_entries():
    # logging.info("Task: Connecting with database")
    cursor, conn = db_connection()
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    columns = [col[0] for col in cursor.description]
    entries = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Assign each column entry to a new variable with the same name as the column name
    data_lists = {col: [] for col in columns}
    for entry in entries:
        for i, col in enumerate(columns):
            data_lists[col].append(entry[i])

    return data_lists


def get_keywords(sentence):
    # logging.info("Task: converting sentence to lower case.")
    # lowered_sentence = sentence.lower()

    logging.info("Task: getting entries from database to validate.")
    db_entries = validate_entries()

    insight_users = db_entries["user"]
    insight_users_lowercase = convert_list_items_to_lowercase(insight_users)

    insight_dates = db_entries["date"]

    # extracted_dates = [date for date in insight_dates if date in lowered_sentence]
    extracted_users = [user for user in insight_users_lowercase if user in lowered_sentence]
    extracted_activity = [activity for activity in action_list if activity in lowered_sentence]
    extracted_platform = [platform for platform in platform_list if platform in lowered_sentence]

    extracted_data = {}

    if extracted_users:
        extracted_data["user"] = extracted_users

    if extracted_activity:
        extracted_data["activity"] = extracted_activity

    if extracted_platform:
        extracted_data["platform"] = extracted_platform

    # if extracted_dates:
    #     extracted_data["date"] = extracted_dates

    if extracted_data:
        logging.info("Task: returning extracted keywords from sentence.")
        return extracted_data

    logging.info("Task: no keywords or platforms extracted from sentence.")
    return "Sorry, could not understand what you are looking for! Please try again."
