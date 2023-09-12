from pathlib import Path

path = Path(__file__).resolve().parent.parent

data_dir = path / "data"
dataset_dir = data_dir / "dataset"
campaign_data = dataset_dir / "unified_data.csv"

db_password = "knoldus"
db_user = "knoldus"
db_host = "localhost"
database = "campaign_data"
table_name = "unified_data"
user_variable = "user"
db_port = 3306

local_model_path = "wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin"

platform_list = ["facebook", "youtube", "instagram"]
action_list = ["views", "clicks", "bought", "subscription", "followers"]

numeric_value_constant = "Task: Getting numerical columns from tha dataframe"
column_name_none = "Task: Checking if column_name is None"
categorical_col_issue = "Sorry can't perform this operation on categorical columns"

categorical_col_check = "Checking is provided column values are categorical"
