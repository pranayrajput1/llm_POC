import numpy as np

from src.utils.constants import numeric_value_constant, column_name_none, categorical_col_check, categorical_col_issue
from src.utils.helpers.input_helpers import get_log

# getting log setup
logging = get_log()


def get_max_value(dataframe, column_name=None):
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


def highest_percent_increase(dataframe, column_name=None):
    """
    Function to calculate the percentage increase from the dataframe and also from a specified column if provided
    @param dataframe
    @param column_name
    @return highest percentage increase
    """
    try:
        logging.info("Task: Get dataframe and calculate the percent increase value from a specific column")

        if column_name is None:
            numeric_columns = dataframe.select_dtypes(include=[float, int]).columns
            old_values = dataframe[numeric_columns].shift(1)
            percentage_increase = ((dataframe[numeric_columns] - old_values) / old_values) * 100
            highest_percentage_increase = percentage_increase.max().max()
        else:
            old_value = dataframe[column_name].shift(1)
            percentage_increase = ((dataframe[column_name] - old_value) / old_value) * 100
            highest_percentage_increase = percentage_increase.max()

        return highest_percentage_increase

    except Exception as e:
        logging.error(f"Some error occurred in calculating the percentage increase, Error: {e}")


def highest_percent_decrease(dataframe, column_name=None):
    """
    Function to calculate the percent decrease from the dataframe and also from a specified column
    @param dataframe
    @param column_name
    @return highest percent decrease
    """
    try:
        logging.info("Task: Get dataframe and calculate the percent decrease value from a specific column")

        if column_name is None:
            numeric_columns = dataframe.select_dtypes(include=[float, int]).columns
            old_values = dataframe[numeric_columns].shift(1)
            percentage_decrease = ((old_values - dataframe[numeric_columns]) / old_values) * 100
            highest_percent_decrease = percentage_decrease.max().max()
        else:
            old_value = dataframe[column_name].shift(1)
            percentage_decrease = ((old_value - dataframe[column_name]) / old_value) * 100
            highest_percent_decrease = percentage_decrease.max()

        return highest_percent_decrease

    except Exception as e:
        logging.error(f"Some error occurred in calculating the percentage decrease, Error: {e}")


def standard_deviation(dataframe, column_name=None):
    """
        Function to calculate the standard deviation from the dataframe and also from a specified column
        @param dataframe
        @param column_name
        @return: Standard deviation value
        """
    try:
        logging.info("Task: Calculate standard deviation from the dataframe")
        numeric_columns = dataframe.select_dtypes(include=[float, int])

        if column_name is None:
            std_whole_dataframe = numeric_columns.stack().std()
            return std_whole_dataframe
        else:
            if column_name in numeric_columns:
                std_single_column = numeric_columns[column_name].std()
                return std_single_column
            else:
                raise ValueError(f"Column '{column_name}' does not exist or is not numeric.")

    except Exception as e:
        logging.error(f"Some error occurred in calculating the standard deviation, Error: {e}")


def calculate_iqr(dataframe, column_name=None):
    """
    Function to calculate the Inter-quartile Range (IQR) from the dataframe and also from a specified column
    @param dataframe
    @param column_name
    @return: IQR value
    """
    try:
        logging.info("Task: Calculate IQR from the dataframe")

        if column_name is None:
            numeric_columns = dataframe.select_dtypes(include=[float, int]).columns
            if 'Index' in numeric_columns:
                numeric_columns = numeric_columns.drop('Index')

            iqr_values = []

            for col in numeric_columns:
                iqr = dataframe[col].quantile(0.75) - dataframe[col].quantile(0.25)
                iqr_values.append((col, iqr))

            return iqr_values
        else:
            iqr_single_column = dataframe[column_name].quantile(0.75) - dataframe[column_name].quantile(0.25)
            return iqr_single_column

    except Exception as e:
        logging.error(f"Some error occurred in calculating the IQR, Error: {e}")


def find_outliers_iqr(dataframe, column_name=None, threshold=1.5):
    """
    Function to find potential outliers using the Inter-quartile Range (IQR) method.
    @param dataframe
    @param column_name
    @param threshold
    @return: List of potential outlier values for specified column
    """
    try:
        logging.info("Task: Find potential outliers using the IQR method")

        outliers_list = []

        if column_name is None:
            numeric_columns = dataframe.select_dtypes(include=[float, int]).columns
            for col in numeric_columns:
                q1 = dataframe[col].quantile(0.25)
                q3 = dataframe[col].quantile(0.75)
                iqr = q3 - q1

                lower_bound = q1 - threshold * iqr
                upper_bound = q3 + threshold * iqr

                outliers = dataframe[(dataframe[col] < lower_bound) | (dataframe[col] > upper_bound)][col]
                outliers_list.extend(outliers.tolist())
        else:
            q1 = dataframe[column_name].quantile(0.25)
            q3 = dataframe[column_name].quantile(0.75)
            iqr = q3 - q1

            lower_bound = q1 - threshold * iqr
            upper_bound = q3 + threshold * iqr

            outliers = dataframe[(dataframe[column_name] < lower_bound) | (dataframe[column_name] > upper_bound)][
                column_name]
            outliers_list.extend(outliers.tolist())

        if len(outliers_list) == 0:
            return None
        else:
            return outliers_list

    except Exception as e:
        logging.error(f"Some error occurred in finding outliers, Error: {e}")


def calculate_median(dataframe, column_name=None):
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


def calculate_covariance(dataframe, column_name=None):
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

        logging.debug(column_name_none)
        if column_name is None:
            logging.debug("Task: Calculating the covariance from the entire dataframe")
            calculated_covariance = dataframe[numeric_columns].cov()
            return calculated_covariance
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
                return column_covariance

    except Exception as e:
        logging.error(f"Some error occurred in calculating covariance, Error: {e}")


def calculate_correlation(dataframe, column_name=None):
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

        logging.debug(column_name_none)
        if column_name is None:
            logging.debug("Task: Calculating the correlation from the entire dataframe")
            calculated_correlation = dataframe[numeric_columns].corr()
            return calculated_correlation

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
                print(column_correlation)
                return column_correlation

    except Exception as e:
        logging.error(f"Some error occurred in calculating covariance, Error: {e}")
