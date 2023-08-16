import pandas as pd
import numpy as np


class DataGenerator:
    def __init__(self, users, dates):
        self.users = users
        self.dates = dates

    def generate_random_data(self):
        """
        allocating random values to the columns.
        return : data
        """
        data = []
        for date in self.dates:
            for user in self.users:
                Facebook_Clicks = np.random.randint(1, 10000)
                Facebook_Views = np.random.randint(1, 10000)
                Facebook_bought = np.random.randint(1, 1000)
                Youtube_Views = np.random.randint(1, 10000)
                Youtube_Clicks = np.random.randint(1, 10000)
                Youtube_Followers = np.random.randint(1, 1000000)
                Youtube_bought = np.random.randint(1, 1000)
                Youtube_Subscription = np.random.randint(1, 100000)
                Instagram_Views = np.random.randint(1, 10000)
                Instagram_Clicks = np.random.randint(1, 10000)
                Instagram_Followers = np.random.randint(1, 1000000)

                data.append(
                    [user, date.date(), Facebook_Clicks, Facebook_Views, Facebook_bought, Youtube_Views, Youtube_Clicks,
                     Youtube_Followers, Youtube_bought, Youtube_Subscription, Instagram_Views, Instagram_Clicks,
                     Instagram_Followers])

        return data

    @staticmethod
    def create_dataframe(data):
        """
        creating dataframe from all the data and adding also adding an index column
        return : df
        """
        df = pd.DataFrame(data, columns=['User', 'Date', 'Facebook_Clicks', 'Facebook_Views', 'Facebook_bought',
                                         'Youtube_Views',
                                         'Youtube_Clicks', 'Youtube_Followers', 'Youtube_bought',
                                         'Youtube_Subscription',
                                         'Instagram_Views', 'Instagram_Clicks', 'Instagram_Followers'])
        start_user_id = 1001
        df.insert(0, 'User ID', range(start_user_id, len(df) + start_user_id))
        return df
