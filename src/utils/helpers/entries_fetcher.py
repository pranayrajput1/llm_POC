from src.utils.constants import table_name
from src.utils.helpers.input_helpers import run_query
from src.utils.helpers.log_setup import get_log

# getting log setup
logging = get_log()


def get_entries(keywords_dictionary):
    extracted_data_entries = {}

    for platform in keywords_dictionary["platform"]:
        for activity_value in keywords_dictionary["activity"]:

            query = f"SELECT {platform+'_'+activity_value} FROM {table_name}"
            extracted_data_entries[platform+'_'+activity_value] = run_query(query)

    return extracted_data_entries
