from random import choices
import pandas as pd


def prepare_origial_dataset_without_target():
    data = pd.read_csv(r'..\data_for_modeling\data\heart_cleveland_upload.csv')
    data = data.drop(columns=['condition'])
    data.to_csv(r'..\data_for_prediction\data\data_sample.csv', index=False)


def prepare_synt_dataset_without_target(size=100, generate_target=False):
    data = pd.read_csv(r'..\data_for_modeling\data\heart_cleveland_upload.csv')
    if not generate_target:
        data = data.drop(columns=['condition'])
    columns = list(data.columns)
    df = pd.DataFrame([], columns=columns)
    for col_name in columns:
        df[col_name] = choices(data[col_name].to_list(), k=size)
    df.to_csv(r'..\data_for_prediction\data\data_synt_sample.csv', index=False)


if __name__ == '__main__':
    prepare_origial_dataset_without_target()
    prepare_synt_dataset_without_target()
