
from src.data.generator.dataset_generator import DataGenerator
from src.utils.constants import campaign_data, users, dates
from src.utils.helpers.input_helpers import get_log

# getting log setup
logging = get_log()


def pipeline():
    """
    calling all the functions and generating a csv file
    return df
    """

    data_generator = DataGenerator(users, dates)
    data = data_generator.generate_random_data()
    df = data_generator.create_dataframe(data)

    logging.info("Task: Created generator and saved to generator folder successfully.")
    df.to_csv(campaign_data, index=False)
    return df
