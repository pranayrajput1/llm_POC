from src.utils.constants import table_name, user_variable
from src.utils.helpers.input_helpers import run_query, get_log

# getting log setup
logging = get_log()


def get_entries(keywords_dictionary):
    extracted_data_entries = {}

    platform_values = keywords_dictionary.get("platform", [])
    activity_values = keywords_dictionary.get("activity", [])
    user_values = keywords_dictionary.get("user", [])
    # dates_values = keywords_dictionary.get("date", [])

    for platform in platform_values:
        for activity in activity_values:
            if len(user_values) == 0:
                query = f"SELECT {platform}_{activity} FROM {table_name}"
                extracted_data_entries[f"{platform}_{activity}"] = run_query(query)
            else:
                for user in user_values:
                    query = f"SELECT {platform}_{activity} FROM {table_name} WHERE {user_variable} = '{user}';"
                    extracted_data_entries[f"{user}_{platform}_{activity}"] = run_query(query)

    return extracted_data_entries


