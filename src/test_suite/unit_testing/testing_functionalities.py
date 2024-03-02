import pandas as pd

from src.utils.constants import campaign_data
from src.utils.helpers.input_helpers import get_log
import unittest

logging = get_log()


class Testing_Functionalities:

    def highest_percent_increase(self, dataframe, column_name=None):
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
                if column_name not in dataframe.columns:
                    return f"Column '{column_name}' does not exist in the dataframe."

                elif dataframe[column_name].dtype.name in ['object', 'category']:
                    return (f"Column '{column_name}' is of categorical nature percentage increase calculation is not "
                            f"suitable for categorical data.")

                old_value = dataframe[column_name].shift(1)
                percentage_increase = ((dataframe[column_name] - old_value) / old_value) * 100
                highest_percentage_increase = percentage_increase.max()

            return highest_percentage_increase

        except Exception as e:
            logging.error(f"Some error occurred in calculating the percentage increase, Error: {e}")

    def highest_percent_decrease(self, dataframe, column_name=None):
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
                if column_name not in dataframe.columns:
                    return f"Column '{column_name}' does not exist in the dataframe."

                elif dataframe[column_name].dtype.name in ['object', 'category']:
                    return (f"Column '{column_name}' is of categorical nature percentage decrease calculation is not "
                            f"suitable for categorical data.")

                old_value = dataframe[column_name].shift(1)
                percentage_decrease = ((old_value - dataframe[column_name]) / old_value) * 100
                highest_percent_decrease = percentage_decrease.max()

            return highest_percent_decrease

        except Exception as e:
            logging.error(f"Some error occurred in calculating the percentage decrease, Error: {e}")

    def standard_deviation(self, dataframe, column_name=None):
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
                if column_name not in dataframe.columns:
                    return f"Column '{column_name}' does not exist in the dataframe."

                elif dataframe[column_name].dtype.name in ['object', 'category']:
                    return (f"Column '{column_name}' is of categorical nature standard deviation calculation is not "
                            f"suitable for categorical data.")

                elif column_name in numeric_columns:
                    std_single_column = numeric_columns[column_name].std()
                    return std_single_column

        except Exception as e:
            logging.error(f"Some error occurred in calculating the standard deviation, Error: {e}")

    def calculate_iqr(self, dataframe, column_name=None):
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
                if column_name not in dataframe.columns:
                    return f"Column '{column_name}' does not exist in the dataframe."

                elif dataframe[column_name].dtype.name in ['object', 'category']:
                    return (f"Column '{column_name}' is of categorical nature. IQR calculation is not "
                            f"suitable for categorical data.")

                iqr_single_column = dataframe[column_name].quantile(0.75) - dataframe[column_name].quantile(0.25)
                return iqr_single_column

        except Exception as e:
            logging.error(f"Some error occurred in calculating the IQR, Error: {e}")

    def find_outliers_iqr(self, dataframe, column_name=None, threshold=1.5):
        """
        Function to find potential outliers using the Interquartile Range (IQR) method.
        @param dataframe
        @param column_name
        @param threshold
        @return: List of potential outlier values for specified column(s)
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
                if column_name not in dataframe.columns:
                    return f"Column '{column_name}' does not exist in the dataframe."

                elif dataframe[column_name].dtype.name in ['object', 'category']:
                    return (f"Column '{column_name}' is of categorical nature. Outliers through IQR calculation is not "
                            f"suitable for categorical data.")

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


class Test_class(unittest.TestCase):
    def test_highest_percent_increase(self):
        data = pd.read_csv(campaign_data)
        df = pd.DataFrame(data)
        testing_func = Testing_Functionalities()

        result = testing_func.highest_percent_increase(df)
        self.assertEqual(result, 87200.0)

        result_column = testing_func.highest_percent_increase(df, 'Facebook_Views')
        self.assertEqual(result_column, 14406.521739130434)

        result1 = testing_func.highest_percent_increase(df,'User')
        self.assertEqual(result1,"Column 'User' is of categorical nature percentage increase calculation is not "
                            f"suitable for categorical data.")

        result2 = testing_func.highest_percent_increase(df,'facebook')
        self.assertEqual(result2,"Column 'facebook' does not exist in the dataframe.")

    def test_highest_percent_decrease(self):
        data = pd.read_csv(campaign_data)
        df = pd.DataFrame(data)
        testing_func = Testing_Functionalities()

        result = testing_func.highest_percent_decrease(df)
        self.assertEqual(result, 99.98635929613968)

        result_column = testing_func.highest_percent_decrease(df, 'Facebook_Clicks')
        self.assertEqual(result_column, 99.62088072324293)

        result1 = testing_func.highest_percent_decrease(df, 'User')
        print(result1)
        self.assertEqual(result1, "Column 'User' is of categorical nature percentage decrease calculation is not "
                            f"suitable for categorical data.")

        result2 = testing_func.highest_percent_increase(df, 'facebook')
        self.assertEqual(result2, "Column 'facebook' does not exist in the dataframe.")

    def test_for_standard_deviation(self):
        data = pd.read_csv(campaign_data)
        df = pd.DataFrame(data)
        testing_func = Testing_Functionalities()

        result = testing_func.standard_deviation(df)
        self.assertEqual(result, 220223.357288199)

        result_column = testing_func.standard_deviation(df, 'Facebook_Clicks')
        self.assertEqual(result_column, 2920.6616063820907)

        result1 = testing_func.standard_deviation(df, 'User')
        self.assertEqual(result1, "Column 'User' is of categorical nature standard deviation calculation is not "
                            f"suitable for categorical data.")

        result2 = testing_func.standard_deviation(df, 'facebook')
        self.assertEqual(result2, "Column 'facebook' does not exist in the dataframe.")

    def test_for_iqr(self):
        data = pd.read_csv(campaign_data)
        df = pd.DataFrame(data)
        testing_func = Testing_Functionalities()

        result = testing_func.calculate_iqr(df)
        self.assertEqual(result, [('Facebook_Clicks', 4916.5), ('Facebook_Views', 4977.75), ('Facebook_bought', 515.5),
                                  ('Youtube_Views', 5411.75), ('Youtube_Clicks', 4807.75),
                                  ('Youtube_Followers', 508882.75), ('Youtube_bought', 496.0),
                                  ('Youtube_Subscription', 47093.0), ('Instagram_Views', 5258.0),
                                  ('Instagram_Clicks', 5227.75), ('Instagram_Followers', 414980.75)])

        result_column = testing_func.calculate_iqr(df, 'Facebook_Clicks')
        self.assertEqual(result_column, 4916.5)

        result1 = testing_func.calculate_iqr(df, 'User')
        self.assertEqual(result1, "Column 'User' is of categorical nature. IQR calculation is not "
                            f"suitable for categorical data.")

        result2 = testing_func.calculate_iqr(df, 'facebook')
        self.assertEqual(result2, "Column 'facebook' does not exist in the dataframe.")

    def test_for_outliers(self):
        data = pd.read_csv(campaign_data)
        df = pd.DataFrame(data)
        testing_func = Testing_Functionalities()

        result = testing_func.find_outliers_iqr(df)
        self.assertEqual(result, None)

        result_column = testing_func.find_outliers_iqr(df, 'Facebook_Clicks')
        self.assertEqual(result_column, None)

        result1 = testing_func.find_outliers_iqr(df, 'User')
        self.assertEqual(result1, "Column 'User' is of categorical nature. Outliers through IQR calculation is not "
                            f"suitable for categorical data.")

        result2 = testing_func.find_outliers_iqr(df, 'facebook')
        self.assertEqual(result2, "Column 'facebook' does not exist in the dataframe.")

