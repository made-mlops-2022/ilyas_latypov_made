import sys
sys.path.insert(0, "../models")
from ml_project.models.modeling import modeling


def test_modeling_logreg():
    X_train, X_test, y_train, y_test, y_train_pred, y_test_pred = \
        modeling(r"../configs/model_lr/modeling.yml")

    assert X_train.shape == (237, 28)
    assert X_test.shape == (60, 28)
    assert y_train.shape == (237, )
    assert y_test.shape == (60, )
    assert y_train_pred.shape == (237, )
    assert y_test_pred.shape == (60, )


def test_modeling_kneighbors_clf():
    X_train, X_test, y_train, y_test, y_train_pred, y_test_pred = \
        modeling(r"../configs/model_kn/modeling.yml")

    assert X_train.shape == (207, 24)
    assert X_test.shape == (90, 24)
    assert y_train.shape == (207,)
    assert y_test.shape == (90,)
    assert y_train_pred.shape == (207,)
    assert y_test_pred.shape == (90,)


if __name__ == '__main__':
    test_modeling_logreg()
    test_modeling_kneighbors_clf()
