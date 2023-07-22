from pathlib import Path

path = Path(__file__).resolve().parent.parent

dataset_dir = path / "dataset"
campaign_data = dataset_dir / "campaign_data.csv"

db_password = "knoldus"
db_user = "knoldus"
db_host = "localhost"
database = "campaign_data"
table_name = "unified_table"
