import numpy as np

from src.utils.constants import numeric_value_constant, column_name_none, categorical_col_check, categorical_col_issue
from src.utils.helpers.log_setup import get_log

# getting log setup
logging = get_log()


def get_max_value(dataframe, column_name=None):
    """
    Function to calculate the maximum value from the data and also for a specific column if provided.
    :param dataframe:
    :param column_name:
    :return: maximum value
    """
    try:

        logging.info("Task: Get dataframe and calculate the maximum value from it, either from whole data or column"
                     "specific")

        logging.debug(numeric_value_constant)
        numeric_columns = dataframe.select_dtypes(include=[np.number]).columns

        logging.debug(column_name_none)
        if column_name is None:
            max_value = dataframe[numeric_columns].max().max()
        else:
            if column_name not in dataframe.columns:
                logging.debug(f"Task: Checking if column_name: {column_name} is in dataframe")
                raise ValueError(f"Column '{column_name}' not found in the DataFrame.")

            elif dataframe[column_name].dtype == 'object':
                logging.debug(categorical_col_check)
                return categorical_col_issue

            else:
                logging.debug(f"Task: Calculating the maximum value from the dataframe column: {column_name}")
                max_value = dataframe[column_name].max()

        logging.debug(f"Task: Returning the maximum value: {max_value}")
        return max_value

    except Exception as e:
        logging.error(f"Some error occurred in getting the maximum value from the data, Error: {e}")


def get_min_value(dataframe, column_name=None):
    """
    Function to calculate the minimum value from the data and also for a specific column if provided.
    @param dataframe:
    @param column_name:
    @return: minimum value
    """
    try:
        logging.info("Task: Get dataframe and calculate the minimum value from it, either from whole data or column "
                     "specific")

        logging.debug(numeric_value_constant)
        numeric_columns = dataframe.select_dtypes(include=[np.number]).columns

        logging.debug(column_name_none)
        if column_name is None:
            min_value = dataframe[numeric_columns].min().min()
        else:
            if column_name not in dataframe.columns:
                logging.debug(f"Task: Checking if column_name: {column_name} is in dataframe")
                raise ValueError(f"Column '{column_name}' not found in the DataFrame.")

            elif dataframe[column_name].dtype == 'object':
                logging.debug(categorical_col_check)
                return categorical_col_issue

            else:
                logging.debug(f"Task: Calculating the minimum value from the dataframe column: {column_name}")
                min_value = dataframe[column_name].min()

        logging.debug(f"Task: Returning the minimum value: {min_value}")
        return min_value

    except Exception as e:
        logging.error(f"Some error occurred in getting the minimum value from the data, Error: {e}")


def get_average(dataframe, column_name=None):
    """
    Function to calculate the average value from the data and also for a specific column if provided.
    @param dataframe:
    @param column_name:
    @return: average value
    """
    try:
        logging.info("Task: Get dataframe and calculate the average value from it, either from whole data or column "
                     "specific")

        logging.debug(numeric_value_constant)
        numeric_columns = dataframe.select_dtypes(include=[np.number]).columns

        logging.debug(column_name_none)
        if column_name is None:
            average_value = dataframe[numeric_columns].mean().mean()
        else:
            if column_name not in dataframe.columns:
                logging.debug(f"Task: Checking if column_name: {column_name} is in dataframe")
                raise ValueError(f"Column '{column_name}' not found in the DataFrame.")

            elif dataframe[column_name].dtype == 'object':
                logging.debug(categorical_col_check)
                return categorical_col_issue

            else:
                logging.debug(f"Task: Calculating the average value from the dataframe column: {column_name}")
                average_value = dataframe[column_name].mean()

        logging.debug(f"Task: Returning the average value: {average_value}")
        average = round(average_value, 2)
        return average

    except Exception as e:
        logging.error(f"Some error occurred in getting the average value from the data, Error: {e}")
