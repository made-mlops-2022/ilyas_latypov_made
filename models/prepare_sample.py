import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv(r'..\data_for_modeling\data\heart_cleveland_upload.csv')
    data = data.drop(columns=['condition'])
    data.to_csv(r'..\data_for_prediction\data\data_sample.csv', index=False)
