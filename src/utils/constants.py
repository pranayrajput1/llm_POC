from pathlib import Path

path = Path(__file__).resolve().parent.parent

dataset_dir = path / "dataset"
campaign_data = dataset_dir / "unified_data.csv"

db_password = "knoldus"
db_user = "knoldus"
db_host = "localhost"
database = "campaign_data"
table_name = "unified_data"

column_keywords = ["user", "date", "facebook_clicks", "facebook_views",
                   "facebook_bought", "youtube_views", "youtube_clicks",
                   "youtube_followers", "youtube_bought", "youtube_subscription",
                   "instagram_views", "instagram_clicks", "instagram_followers"]

platform_list = ["facebook", "youtube", "instagram"]
action_list = ["views", "clicks", "bought", "subscription", "followers"]
