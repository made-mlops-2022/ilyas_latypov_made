import sys
sys.path.insert(0, "../models")
from ml_project.models.features import features_prepare
from ml_project.models.modeling import modeling
from ml_project.models.prediction import prediction


def test_pipeline_logreg():
    x_num, x_cat, target = \
        features_prepare(r"../configs/model_lr/features.yml")
    X_train, X_test, y_train, y_test, y_train_pred, y_test_pred = \
        modeling(r"../configs/model_lr/modeling.yml")
    predict_target = \
        prediction(r"../configs/model_lr/predict.yml")

    assert X_train.shape == (237, 28)
    assert X_test.shape == (60, 28)
    assert y_train.shape == (237, )
    assert y_test.shape == (60, )
    assert y_train_pred.shape == (237, )
    assert y_test_pred.shape == (60, )
    assert x_num.shape == (297, 5)
    assert x_cat.shape == (297, 23)
    assert target.shape == (297, 1)
    assert predict_target.shape == (297, 1)


def test_modeling_kneighbors_clf():
    x_num, x_cat, target = \
        features_prepare(r"../configs/model_kn/features.yml")
    X_train, X_test, y_train, y_test, y_train_pred, y_test_pred = \
        modeling(r"../configs/model_kn/modeling.yml")
    predict_target = \
        prediction(r"../configs/model_kn/predict.yml")

    assert X_train.shape == (207, 24)
    assert X_test.shape == (90, 24)
    assert y_train.shape == (207,)
    assert y_test.shape == (90,)
    assert y_train_pred.shape == (207,)
    assert y_test_pred.shape == (90,)
    assert x_num.shape == (297, 4)
    assert x_cat.shape == (297, 20)
    assert target.shape == (297, 1)
    assert predict_target.shape == (297, 1)


if __name__ == '__main__':
    test_pipeline_logreg()
    test_modeling_kneighbors_clf()
