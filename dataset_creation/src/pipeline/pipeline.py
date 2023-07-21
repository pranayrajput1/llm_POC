import pandas as pd

from dataset_creation.src.creating_dataset.dataset import DataGenerator


def pipeline():
    """
    calling all the functions and generating a csv file
    return df
    """
    users = ['Ram', 'Aman', 'Durgesh']
    dates = pd.date_range(start='2023-01-01', end='2023-03-01', freq='D')

    data_generator = DataGenerator(users, dates)
    data = data_generator.generate_random_data()
    df = data_generator.create_dataframe(data)

    df.to_csv('unified_data.csv', index=False)
    return df