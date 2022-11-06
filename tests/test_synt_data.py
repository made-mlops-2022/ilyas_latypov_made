import sys
sys.path.insert(0, "../models")
import pandas as pd
from ml_project.models.prepare_sample import prepare_origial_dataset_without_target
from ml_project.models.prepare_sample import prepare_synt_dataset_without_target


def test_prepare_origial_dataset_without_target():
    prepare_origial_dataset_without_target()
    data = pd.read_csv(r'..\data_for_prediction\data\data_sample.csv')
    assert data.shape == (297, 13)


def test_prepare_synt_dataset_without_target():
    prepare_synt_dataset_without_target(size=150)
    data = pd.read_csv(r'..\data_for_prediction\data\data_synt_sample.csv')
    assert data.shape == (150, 13)


if __name__ == '__main__':
    test_prepare_origial_dataset_without_target()
    test_prepare_synt_dataset_without_target()
