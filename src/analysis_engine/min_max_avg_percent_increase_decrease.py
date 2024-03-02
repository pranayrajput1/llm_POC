import numpy as np
import pandas as pd

from src.utils.constants import numeric_value_constant, column_name_none, categorical_col_check, categorical_col_issue, \
    primary_key, intervals, threshold
from src.utils.helpers.input_helpers import get_log

# getting log setup
logging = get_log()


def get_max_value(dataframe, column_name=None, interval=None):
    """
    Function to calculate the maximum value from the data and also for a specific column if provided.
    @param dataframe:
    @param column_name:
    @return: maximum value
    """
    try:

        logging.info("Task: Get dataframe and calculate the maximum value from it, either from whole data or column"
                     "specific")

        logging.debug(numeric_value_constant)
        numeric_columns = dataframe.select_dtypes(include=[np.number]).columns
        numeric_columns = numeric_columns.drop(primary_key)

        logging.debug(column_name_none)
        if column_name is None:
            max_value = dataframe[numeric_columns].max().max()
            column_with_max = dataframe[numeric_columns].max().idxmax()
            logging.debug(f"Task: Returning the maximum value: {max_value} from column: {column_with_max}")
            return max_value, column_with_max
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


def get_min_value(dataframe, column_name=None, interval=None):
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
        numeric_columns = numeric_columns.drop(primary_key)

        logging.debug(column_name_none)
        if column_name is None:
            min_value = dataframe[numeric_columns].min().min()
            column_with_min = dataframe[numeric_columns].min().idxmin()
            logging.debug(f"Task: Returning the minimum value: {min_value} from column: {column_with_min}")
            return min_value, column_with_min
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


def get_average(dataframe, column_name=None, interval=None):
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
        numeric_columns = numeric_columns.drop(primary_key)

        logging.debug(column_name_none)
        if column_name is None:
            average_value = dataframe[numeric_columns].mean().mean()
            column_with_average = dataframe[numeric_columns].mean().idxmin()
            logging.debug(f"Task: Returning the average value: {average_value} from column: {column_with_average}")
            return average_value, column_with_average
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


def highest_percent_increase(dataframe, column_name=None, interval=None):
    """
    Function to calculate the percentage increase from the dataframe and also from a specified column if provided
    @param dataframe
    @param column_name
    @return highest percentage increase
    :param interval:
    :param interval:
    """
    try:
        logging.info("Task: Get dataframe and calculate the percent increase value from a specific column")
        numeric_columns = dataframe.select_dtypes(include=[np.number]).columns
        numeric_columns = numeric_columns.drop(primary_key)
        dataframe['Date'] = pd.to_datetime(dataframe['Date'])
        dataframe.set_index('Date', inplace=True)

        if column_name is None:
            resampled_df = dataframe[numeric_columns].resample(interval).last()
            percentage_increase = ((resampled_df - resampled_df.shift(1)) / resampled_df.shift(1)) * 100
            highest_percentage_increase = percentage_increase.max().max()
        else:
            if column_name not in dataframe.columns:
                return f"Column '{column_name}' does not exist in the dataframe."

            elif dataframe[column_name].dtype.name in ['object', 'category']:
                return (f"Column '{column_name}' is of categorical nature; percentage increase calculation is not "
                        f"suitable for categorical data.")

            resampled_col = dataframe[column_name].resample(interval).last()
            percentage_increase = ((resampled_col - resampled_col.shift(1)) / resampled_col.shift(1)) * 100
            highest_percentage_increase = percentage_increase.max()

        return highest_percentage_increase

    except Exception as e:
        logging.error(f"Some error occurred in calculating the percentage increase, Error: {e}")


def highest_percent_decrease(dataframe, column_name=None, interval=None):
    """
    Function to calculate the percent decrease from the dataframe and also from a specified column
    @param dataframe
    @param column_name
    @return highest percent decrease
    """
    try:
        logging.info("Task: Get dataframe and calculate the percent decrease value from a specific column")
        numeric_columns = dataframe.select_dtypes(include=[np.number]).columns
        numeric_columns = numeric_columns.drop(primary_key)
        dataframe['Date'] = pd.to_datetime(dataframe['Date'])
        dataframe.set_index('Date', inplace=True)

        if column_name is None:
            resampled_df = dataframe[numeric_columns].resample(interval).last()
            percentage_decrease = ((resampled_df.shift(1)) - resampled_df / resampled_df.shift(1)) * 100
            highest_percent_decrease = percentage_decrease.max().max()
        else:
            if column_name not in dataframe.columns:
                return f"Column '{column_name}' does not exist in the dataframe."

            elif dataframe[column_name].dtype.name in ['object', 'category']:
                return (f"Column '{column_name}' is of categorical nature percentage decrease calculation is not "
                        f"suitable for categorical data.")

            resampled_col = dataframe[column_name].resample(interval).last()
            percentage_decrease = ((resampled_col.shift(1)) - resampled_col / resampled_col.shift(1)) * 100
            highest_percent_decrease = percentage_decrease.max()

        return highest_percent_decrease

    except Exception as e:
        logging.error(f"Some error occurred in calculating the percentage decrease, Error: {e}")


def standard_deviation(dataframe, column_name=None, interval=None):
    """
        Function to calculate the standard deviation from the dataframe and also from a specified column
        @param dataframe
        @param column_name
        @return: Standard deviation value
        """
    try:
        logging.info("Task: Calculate standard deviation from the dataframe")
        numeric_columns = dataframe.select_dtypes(include=[np.number]).columns
        numeric_columns = numeric_columns.drop(primary_key)

        if column_name is None:
            std_whole_dataframe = dataframe[numeric_columns].std().max()
            column_with_max_std = dataframe[numeric_columns].std().idxmax()
            return std_whole_dataframe, column_with_max_std
        else:
            if column_name not in dataframe.columns:
                return f"Column '{column_name}' does not exist in the dataframe."

            elif dataframe[column_name].dtype.name in ['object', 'category']:
                return (f"Column '{column_name}' is of categorical nature. "
                        f"Standard deviation calculation is not suitable for categorical data.")

            elif column_name in numeric_columns:
                std_single_column = dataframe[column_name].std()
                return std_single_column

    except Exception as e:
        logging.error(f"Some error occurred in calculating the standard deviation, Error: {e}")


def calculate_iqr(dataframe, column_name=None, interval=None):
    """
    Function to calculate the Inter-quartile Range (IQR) from the dataframe and also from a specified column
    @param dataframe
    @param column_name
    @return: IQR value
    """
    try:
        logging.info("Task: Calculate IQR from the dataframe")

        if column_name is None:
            numeric_columns = dataframe.select_dtypes(include=[np.number]).columns
            numeric_columns = numeric_columns.drop(primary_key)

            iqr_values = []
            # how spread your data is
            for col in numeric_columns:
                iqr = dataframe[col].quantile(0.75) - dataframe[col].quantile(0.25)
                iqr_values.append((col, iqr))

            return iqr_values
        else:
            if column_name not in dataframe.columns:
                return f"Column '{column_name}' does not exist in the dataframe."

            elif dataframe[column_name].dtype.name in ['object', 'category']:
                return (f"Column '{column_name}' is of categorical nature. IQR calculation is not "
                        f"suitable for categorical data.")

            iqr_single_column = dataframe[column_name].quantile(0.75) - dataframe[column_name].quantile(0.25)
            return iqr_single_column

    except Exception as e:
        logging.error(f"Some error occurred in calculating the IQR, Error: {e}")


def find_outliers_iqr(dataframe, column_name=None, interval=None):
    """
    Function to find potential outliers using the Inter-quartile Range (IQR) method.
    @param dataframe
    @param column_name
    @return: List of potential outlier values for specified column
    """
    try:
        logging.info("Task: Find potential outliers using the IQR method")
        numeric_columns = dataframe.select_dtypes(include=[np.number]).columns
        numeric_columns = numeric_columns.drop(primary_key)
        outliers_list = []

        if column_name is None:
            for col in numeric_columns:
                q1 = dataframe[col].quantile(0.25)
                q3 = dataframe[col].quantile(0.75)
                iqr = q3 - q1

                lower_bound = q1 - threshold * iqr
                upper_bound = q3 + threshold * iqr

                outliers = dataframe[(dataframe[col] < lower_bound) | (dataframe[col] > upper_bound)][col]
                outliers_list.extend(outliers.tolist())
        else:
            if column_name not in dataframe.columns:
                return f"Column '{column_name}' does not exist in the dataframe."

            elif dataframe[column_name].dtype.name in ['object', 'category']:
                return (f"Column '{column_name}' is of categorical nature. Outliers through IQR calculation is not "
                        f"suitable for categorical data.")

            q1 = dataframe[column_name].quantile(0.25)
            q3 = dataframe[column_name].quantile(0.75)
            iqr = q3 - q1

            lower_bound = q1 - (threshold * iqr)
            upper_bound = q3 + (threshold * iqr)

            outliers = dataframe[(dataframe[column_name] < lower_bound) | (dataframe[column_name] > upper_bound)][
                column_name]
            outliers_list.extend(outliers.tolist())

        if len(outliers_list) == 0:
            return None
        else:
            return outliers_list

    except Exception as e:
        logging.error(f"Some error occurred in finding outliers, Error: {e}")


def calculate_median(dataframe, column_name=None, interval=None):
    """
    Function to calculate median of the dataframe and median
    of a single feature from the dataframe if provided
    @param dataframe: entire dataframe
    @param column_name: column name if provided else none
    @return: calculated median
    """
    try:
        logging.info("Task: Get dataframe and calculate the median from it, either from whole data or column"
                     "specific")

        logging.debug(numeric_value_constant)
        numeric_columns = dataframe.select_dtypes(include=[np.number]).columns
        numeric_columns = numeric_columns.drop(primary_key)

        if column_name is None:
            logging.debug("Task: Calculating the median from the entire dataframe")
            calculated_median = np.median(dataframe[numeric_columns].values)
            return calculated_median
        else:
            if column_name not in dataframe.columns:
                logging.debug(f"Task: Checking if column_name: {column_name} is in dataframe")
                raise ValueError(f"Column '{column_name}' does not exists in dataframe.")

            elif dataframe[column_name].dtype == 'object':
                logging.debug(categorical_col_check)
                raise ValueError(categorical_col_issue)

            else:
                logging.debug(f"Task: Calculating the median from the dataframe column: {column_name}")
                column_median = np.median(dataframe[column_name])
                return column_median

    except Exception as e:
        logging.error(f"Some error occurred in calculating median, Error: {e}")


def calculate_covariance(dataframe, column_name=None, interval=None):
    """
    Function to calculate covariance of the dataframe and covariance
    of a single columns from the dataframe if provided
    @param dataframe: entire dataframe
    @param column_name: column name if provided else none
    @return: calculated covariance
    """
    try:
        logging.info("Task: Get dataframe and calculate the covariance from it, either from whole data or column"
                     "specific")

        logging.debug(numeric_value_constant)
        numeric_columns = dataframe.select_dtypes(include=[np.number]).columns
        numeric_columns = numeric_columns.drop(primary_key)

        logging.debug(column_name_none)
        if column_name is None:
            logging.debug("Task: Calculating the covariance from the entire dataframe")
            calculated_covariance = dataframe[numeric_columns].cov()
            return calculated_covariance.to_dict()
        else:
            logging.debug(f"Columns name is provided: '{column_name}'")
            if column_name not in dataframe.columns:
                logging.debug(f"Task: Checking if column_name: {column_name} is in dataframe")
                raise ValueError(f"Column '{column_name}' does not exists in dataframe.")

            elif dataframe[column_name].dtype == 'object':
                logging.debug(categorical_col_check)
                raise ValueError(categorical_col_issue)

            else:
                logging.debug(f"Task: Calculating the covariance from the dataframe column: {column_name}")
                column_covariance = dataframe[numeric_columns].cov().loc[column_name]
                return column_covariance.to_dict()

    except Exception as e:
        logging.error(f"Some error occurred in calculating covariance, Error: {e}")


def calculate_correlation(dataframe, column_name=None, interval=None):
    """
    Function to calculate correlation of the dataframe and covariance
    of a single columns from the dataframe if provided
    @param dataframe: entire dataframe
    @param column_name: column name if provided else none
    @return: calculated covariance
    """
    try:
        logging.info("Task: Get dataframe and calculate the correlation from it, either from whole data or column"
                     "specific")

        logging.debug(numeric_value_constant)
        numeric_columns = dataframe.select_dtypes(include=[np.number]).columns
        numeric_columns = numeric_columns.drop(primary_key)

        logging.debug(column_name_none)
        if column_name is None:
            logging.debug("Task: Calculating the correlation from the entire dataframe")
            calculated_correlation = dataframe[numeric_columns].corr()
            return calculated_correlation.to_dict()

        else:
            logging.debug(f"Columns name is provided: '{column_name}'")
            if column_name not in dataframe.columns:
                logging.debug(f"Task: Checking if column_name: {column_name} is in dataframe")
                raise ValueError(f"Column '{column_name}' does not exists in dataframe.")

            elif dataframe[column_name].dtype == 'object':
                logging.debug(categorical_col_check)
                raise ValueError(categorical_col_issue)

            else:
                logging.debug(f"Task: Calculating the correlation from the dataframe column: {column_name}")
                column_correlation = dataframe[numeric_columns].corr().loc[column_name]

                return column_correlation.to_dict()

    except Exception as e:
        logging.error(f"Some error occurred in calculating covariance, Error: {e}")
