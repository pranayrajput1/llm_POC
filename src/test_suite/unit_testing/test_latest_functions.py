import numpy as np
import pandas as pd
from src.test_suite.test_sample.test_sample_df import sample_dataframe
from src.utils.constants import numeric_value_constant, column_name_none, categorical_col_issue, categorical_col_check
import unittest
from pytest import fixture

from src.utils.helpers.input_helpers import get_log

# getting log setup
logging = get_log()


@fixture
def dataframe():
    test_df = pd.DataFrame(sample_dataframe)
    return test_df


def test_get_max_value(dataframe, column_name=None):
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
        numeric_columns = numeric_columns.drop('Index')

        logging.debug(column_name_none)
        if column_name is None:
            max_value = dataframe[numeric_columns].max().max()
        else:
            if column_name not in dataframe.columns:
                logging.debug(f"Task: Checking if column_name: {column_name} is in dataframe")
                return f"Column '{column_name}' not found in the DataFrame."

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


def test_get_min_value(dataframe, column_name=None):
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
        numeric_columns = numeric_columns.drop('Index')

        logging.debug(column_name_none)
        if column_name is None:
            min_value = dataframe[numeric_columns].min().min()
        else:
            if column_name not in dataframe.columns:
                logging.debug(f"Task: Checking if column_name: {column_name} is in dataframe")
                return f"Column '{column_name}' not found in the DataFrame."

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


def test_get_average(dataframe, column_name=None):
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
        numeric_columns = numeric_columns.drop('Index')

        logging.debug(column_name_none)
        if column_name is None:
            average_value = dataframe[numeric_columns].mean().mean()
        else:
            if column_name not in dataframe.columns:
                logging.debug(f"Task: Checking if column_name: {column_name} is in dataframe")
                return f"Column '{column_name}' not found in the DataFrame."

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


def test_calculate_median(dataframe, column_name=None):
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
        numeric_columns = numeric_columns.drop('Index')

        if column_name is None:
            logging.debug("Task: Calculating the median from the entire dataframe")
            calculated_median = np.median(dataframe[numeric_columns].values)
            return calculated_median
        else:
            if column_name not in dataframe.columns:
                logging.debug(f"Task: Checking if column_name: {column_name} is in dataframe")
                return f"Column '{column_name}' does not exists in dataframe."

            elif dataframe[column_name].dtype == 'object':
                logging.debug(categorical_col_check)
                return categorical_col_issue

            else:
                logging.debug(f"Task: Calculating the median from the dataframe column: {column_name}")
                column_median = np.median(dataframe[column_name])
                return column_median

    except Exception as e:
        logging.error(f"Some error occurred in calculating median, Error: {e}")


def test_calculate_covariance(dataframe, column_name=None):
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
        numeric_columns = numeric_columns.drop('Index')

        logging.debug(column_name_none)
        if column_name is None:
            logging.debug("Task: Calculating the covariance from the entire dataframe")
            calculated_covariance = dataframe[numeric_columns].cov()
            return calculated_covariance.to_dict()
        else:
            logging.debug(f"Columns name is provided: '{column_name}'")
            if column_name not in dataframe.columns:
                logging.debug(f"Task: Checking if column_name: {column_name} is in dataframe")
                return f"Column '{column_name}' does not exists in dataframe."

            elif dataframe[column_name].dtype == 'object':
                logging.debug(categorical_col_check)
                return categorical_col_issue

            else:
                logging.debug(f"Task: Calculating the covariance from the dataframe column: {column_name}")
                column_covariance = dataframe[numeric_columns].cov().loc[column_name]
                return column_covariance.to_dict()

    except Exception as e:
        logging.error(f"Some error occurred in calculating covariance, Error: {e}")


def test_calculate_correlation(dataframe, column_name=None):
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
        numeric_columns = numeric_columns.drop('Index')

        logging.debug(column_name_none)
        if column_name is None:
            logging.debug("Task: Calculating the correlation from the entire dataframe")
            calculated_correlation = dataframe[numeric_columns].corr()
            return calculated_correlation.to_dict()

        else:
            logging.debug(f"Columns name is provided: '{column_name}'")
            if column_name not in dataframe.columns:
                logging.debug(f"Task: Checking if column_name: {column_name} is in dataframe")
                return f"Column '{column_name}' does not exists in dataframe."

            elif dataframe[column_name].dtype == 'object':
                logging.debug(categorical_col_check)
                return categorical_col_issue

            else:
                logging.debug(f"Task: Calculating the correlation from the dataframe column: {column_name}")
                column_correlation = dataframe[numeric_columns].corr().loc[column_name]
                return column_correlation.to_dict()

    except Exception as e:
        logging.error(f"Some error occurred in calculating covariance, Error: {e}")


class AnalysisEngineTest(unittest.TestCase):

    def test_one_for_max_value(self):
        data_frame = pd.DataFrame(sample_dataframe)
        response = test_get_max_value(data_frame)
        self.assertEqual(response, 78)

    def test_two_for_max_value(self):
        data_frame = pd.DataFrame(sample_dataframe)
        response = test_get_max_value(data_frame, "views")
        self.assertEqual(response, 45)

    def test_three_for_max_value(self):
        data_frame = pd.DataFrame(sample_dataframe)
        response = test_get_max_value(data_frame, "name")
        self.assertEqual(response, categorical_col_issue)

    def test_four_for_max_value(self):
        data_frame = pd.DataFrame(sample_dataframe)
        col_name = "unknown"
        response = test_get_max_value(data_frame, col_name)
        self.assertEqual(response, f"Column '{col_name}' not found in the DataFrame.")

    def test_one_for_min_value(self):
        data_frame = pd.DataFrame(sample_dataframe)
        response = test_get_min_value(data_frame)
        self.assertEqual(response, 1)

    def test_two_for_min_value(self):
        data_frame = pd.DataFrame(sample_dataframe)
        response = test_get_min_value(data_frame, "clicks")
        self.assertEqual(response, 2)

    def test_three_for_min_value(self):
        data_frame = pd.DataFrame(sample_dataframe)
        response = test_get_min_value(data_frame, "name")
        self.assertEqual(response, categorical_col_issue)

    def test_four_for_min_value(self):
        data_frame = pd.DataFrame(sample_dataframe)
        col_name = "random"
        response = test_get_min_value(data_frame, col_name)
        self.assertEqual(response, f"Column '{col_name}' not found in the DataFrame.")

    def test_one_for_avg_value(self):
        data_frame = pd.DataFrame(sample_dataframe)
        response = test_get_average(data_frame)
        self.assertEqual(response, 21.95)

    def test_two_for_avg_value(self):
        data_frame = pd.DataFrame(sample_dataframe)
        response = test_get_average(data_frame, "bought")
        self.assertEqual(response, 18.2)

    def test_three_for_avg_value(self):
        data_frame = pd.DataFrame(sample_dataframe)
        response = test_get_average(data_frame, "name")
        self.assertEqual(response, categorical_col_issue)

    def test_four_for_avg_value(self):
        data_frame = pd.DataFrame(sample_dataframe)
        col_name = "some_col"
        response = test_get_average(data_frame, col_name)
        self.assertEqual(response, f"Column '{col_name}' not found in the DataFrame.")

    def test_one_for_median(self):
        data_frame = pd.DataFrame(sample_dataframe)
        col_name = "some_col"
        response = test_calculate_median(data_frame, col_name)
        self.assertEqual(response, f"Column '{col_name}' does not exists in dataframe.")

    def test_two_for_median(self):
        data_frame = pd.DataFrame(sample_dataframe)
        response = test_calculate_median(data_frame)

        numeric_columns = data_frame.select_dtypes(include=[np.number]).columns
        numeric_columns = numeric_columns.drop('Index')

        calculated_median = np.median(data_frame[numeric_columns].values)
        self.assertEqual(response, calculated_median)

    def test_three_for_median(self):
        data_frame = pd.DataFrame(sample_dataframe)
        response = test_calculate_median(data_frame, "name")
        self.assertEqual(response, categorical_col_issue)

    def test_four_for_median(self):
        data_frame = pd.DataFrame(sample_dataframe)
        response = test_calculate_median(data_frame, "clicks")

        column_name = "clicks"
        column_median = np.median(data_frame[column_name])
        self.assertEqual(response, column_median)

    def test_one_for_covariance(self):
        data_frame = pd.DataFrame(sample_dataframe)
        col_name = "some_col"
        response = test_calculate_covariance(data_frame, col_name)
        self.assertEqual(response, f"Column '{col_name}' does not exists in dataframe.")

    def test_two_for_covariance(self):
        data_frame = pd.DataFrame(sample_dataframe)
        response = test_calculate_covariance(data_frame)

        numeric_columns = data_frame.select_dtypes(include=[np.number]).columns
        numeric_columns = numeric_columns.drop('Index')

        calculated_covariance = data_frame[numeric_columns].cov()
        self.assertTrue(response, calculated_covariance.to_dict())

    def test_three_for_covariance(self):
        data_frame = pd.DataFrame(sample_dataframe)
        response = test_calculate_covariance(data_frame, "name")
        self.assertEqual(response, categorical_col_issue)

    def test_four_for_covariance(self):
        data_frame = pd.DataFrame(sample_dataframe)
        column_name = "clicks"

        response = test_calculate_covariance(data_frame, column_name)

        numeric_columns = data_frame.select_dtypes(include=[np.number]).columns
        numeric_columns = numeric_columns.drop('Index')

        column_covariance = data_frame[numeric_columns].cov().loc[column_name]
        self.assertEqual(response, column_covariance.to_dict())

    def test_one_for_correlation(self):
        data_frame = pd.DataFrame(sample_dataframe)
        col_name = "some_col"
        response = test_calculate_correlation(data_frame, col_name)
        self.assertEqual(response, f"Column '{col_name}' does not exists in dataframe.")

    def test_two_for_correlation(self):
        data_frame = pd.DataFrame(sample_dataframe)
        response = test_calculate_correlation(data_frame)

        numeric_columns = data_frame.select_dtypes(include=[np.number]).columns
        numeric_columns = numeric_columns.drop('Index')

        calculated_correlation = data_frame[numeric_columns].corr()
        self.assertTrue(response, calculated_correlation.to_dict())

    def test_three_for_correlation(self):
        data_frame = pd.DataFrame(sample_dataframe)
        response = test_calculate_correlation(data_frame, "name")
        self.assertEqual(response, categorical_col_issue)

    def test_four_for_correlation(self):
        data_frame = pd.DataFrame(sample_dataframe)
        column_name = "clicks"

        response = test_calculate_correlation(data_frame, column_name)

        numeric_columns = data_frame.select_dtypes(include=[np.number]).columns
        numeric_columns = numeric_columns.drop('Index')

        column_correlation = data_frame[numeric_columns].corr().loc[column_name]
        self.assertEqual(response, column_correlation.to_dict())


if __name__ == '__main__':
    unittest.main()
