import sys
sys.path.insert(0, "../models")
from ml_project.models.features import features_prepare


def test_features_modeling_for_logreg():
    x_num, x_cat, target =\
        features_prepare(r"../configs/model_lr/features.yml")

    assert x_num.shape == (297, 5)
    assert x_cat.shape == (297, 23)
    assert target.shape == (297, 1)


def test_features_modeling_for_kneighbors_clf():
    x_num, x_cat, target =\
        features_prepare(r"../configs/model_kn/features.yml")

    assert x_num.shape == (297, 4)
    assert x_cat.shape == (297, 20)
    assert target.shape == (297, 1)


if __name__ == '__main__':
    test_features_modeling_for_logreg()
    test_features_modeling_for_kneighbors_clf()
