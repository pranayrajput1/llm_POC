from pathlib import Path

import pandas as pd

path = Path(__file__).resolve().parent.parent

data_dir = path / "data"
dataset_dir = data_dir / "dataset"
campaign_data = dataset_dir / "unified_data.csv"

db_password = "sanskriti"
db_user = "sanskriti"
db_host = "localhost"
database = "campaign_data"
table_name = "unified_data"
user_variable = "user"

platform_list = ["facebook", "youtube", "instagram"]
action_list = ["views", "clicks", "bought", "subscription", "followers"]

users = ['Ram', 'Aman', 'Durgesh']
dates = pd.date_range(start='2023-01-01', end='2023-03-01', freq='D')

primary_key = "User ID"
intervals = ['W']

# dataset all columns
columns = ['User', 'Date', 'Facebook_Clicks', 'Facebook_Views', 'Facebook_bought',
           'Youtube_Views',
           'Youtube_Clicks', 'Youtube_Followers', 'Youtube_bought',
           'Youtube_Subscription',
           'Instagram_Views', 'Instagram_Clicks', 'Instagram_Followers']

# operations in analysis engine
operations = ["highest", "lowest", "average", "greatest", "peak", "least", "percent increase",
              "percent decrease", "standard deviation", "IQR", "Outliers", "median", "covariance",
              "correlation"]

# numeric columns in the dataframe
dataframe_columns = ["Facebook_Clicks", "Facebook_Views", "Facebook_bought", "Youtube_Views",
                     "Youtube_Clicks", "Youtube_Followers", "Youtube_bought", "Youtube_Subscription",
                     "Instagram_Views", "Instagram_Clicks", "Instagram_Followers"]

# threshold for function finding outliers using IQR function
threshold = 1.5

numeric_value_constant = "Task: Getting numerical columns from tha dataframe"
column_name_none = "Task: Checking if column_name is None"
categorical_col_issue = "Sorry can't perform this operation on categorical columns"

categorical_col_check = "Checking is provided column values are categorical"
