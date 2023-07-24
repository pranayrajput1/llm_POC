import numpy as np


def get_max_value(dataframe, column_name=None):
    """
    Function to calculate the maximum value from the data and also for a specific column if provided.
    :param dataframe:
    :param column_name:
    :return: maximum value
    """
    numeric_columns = dataframe.select_dtypes(include=[np.number]).columns

    if column_name is None:
        max_value = dataframe[numeric_columns].max().max()
    else:
        if column_name not in dataframe.columns:
            raise ValueError(f"Column '{column_name}' not found in the DataFrame.")
        max_value = dataframe[column_name].max()

    return max_value


def get_min_value(dataframe, column_name=None):
    """
    Function to calculate the minimum value from the data and also for a specific column if provided.
    :param dataframe:
    :param column_name:
    :return: minimum value
    """
    numeric_columns = dataframe.select_dtypes(include=[np.number]).columns

    if column_name is None:
        min_value = dataframe[numeric_columns].min().min()
    else:
        if column_name not in dataframe.columns:
            raise ValueError(f"Column '{column_name}' not found in the DataFrame.")
        min_value = dataframe[column_name].min()

    return min_value


def get_average(dataframe, column_name=None):
    """
    Function to calculate the average value from the data and also for a specific column if provided.
    :param dataframe:
    :param column_name:
    :return: average value
    """

    numeric_columns = dataframe.select_dtypes(include=[np.number]).columns

    if column_name is None:
        average_value = dataframe[numeric_columns].mean().mean()
    else:
        if column_name not in dataframe.columns:
            raise ValueError(f"Column '{column_name}' not found in the DataFrame.")
        average_value = dataframe[column_name].mean()

    return average_value
