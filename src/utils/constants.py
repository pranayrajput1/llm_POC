from pathlib import Path

path = Path(__file__).resolve().parent.parent

dataset_dir = path / "dataset"
campaign_data = dataset_dir / "unified_data.csv"

db_password = "sanskriti"
db_user = "sanskriti"
db_host = "localhost"
database = "campaign_data"
table_name = "unified_data"
user_variable = "user"

platform_list = ["facebook", "youtube", "instagram"]
action_list = ["views", "clicks", "bought", "subscription", "followers"]

numeric_value_constant = "Task: Getting numerical columns from tha dataframe"
column_name_none = "Task: Checking if column_name is None"
categorical_col_issue = "Sorry can't perform the maximum operation on categorical columns"

categorical_col_check = "Checking is provided column values are categorical"
