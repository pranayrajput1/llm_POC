import pandas as pd

from src.data.dataset.dataset_generator import DataGenerator
from src.utils.constants import campaign_data
from src.utils.helpers.input_helpers import get_log

# getting log setup
logging = get_log()


def pipeline():
    """
    calling all the functions and generating a csv file
    return df
    """
    users = ['Ram', 'Aman', 'Durgesh']
    dates = pd.date_range(start='2023-01-01', end='2023-03-01', freq='D')

    data_generator = DataGenerator(users, dates)
    data = data_generator.generate_random_data()
    df = data_generator.create_dataframe(data)

    logging.info("Task: Created dataset and saved to dataset folder successfully.")
    df.to_csv(campaign_data, index=False)
    return df
