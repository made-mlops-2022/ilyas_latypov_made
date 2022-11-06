import sys
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import roc_auc_score
from config import read_config_model_params
from logger import start_logger


def modeling():
    if len(sys.argv) != 2:
        print("Specify the config file as а parameter")
        return
    model_par = read_config_model_params(sys.argv[1])
    logger = start_logger(model_par.root_path + model_par.logging_path)
    logger.info("Инициализация логирования и загрузка файла параметров")

    logger.debug("Загрузка данных")
    x_num = pd.read_csv(model_par.root_path + model_par.data_path_num_features).values
    x_cat = pd.read_csv(model_par.root_path + model_par.data_path_cat_features).values
    target = pd.read_csv(model_par.root_path + model_par.data_path_target_path).values.ravel()
    x_num_cat = np.hstack((x_num, x_cat))

    logger.debug("Разделение данных на трейн и тест")
    X_train, X_test, y_train, y_test = train_test_split(x_num_cat,
                                                        target,
                                                        test_size=model_par.test_size,
                                                        random_state=model_par.seed)
    model_name = model_par.model_name
    if model_name in ["KNeighborsClassifier", "LogisticRegression"]:
        logger.debug("Расчет модели %s", model_name)
        print(model_name + ":")
        params = dict()
        if model_name == "LogisticRegression":
            params[model_par.model_param_name] = model_par.model_param_value
            params['random_state'] = model_par.seed
        else:
            params[model_par.model_param_name] = int(model_par.model_param_value)

        logger.debug("Настройка модели %s", model_name)
        estimator = eval(model_par.model_name)(**params)
        estimator.fit(X_train, y_train)
        msg = "roc_auc_train: "
        msg += str(round(roc_auc_score(y_train, estimator.predict_proba(X_train)[:, 1]), 4))
        print(msg)
        logger.info(msg)

        msg = "roc_auc_test: "
        msg += str(round(roc_auc_score(y_test, estimator.predict_proba(X_test)[:, 1]), 4))
        print(msg)
        logger.info(msg)

        logger.debug("Сохранение модели(pkl) %s", model_name)
        model_filename = model_par.root_path + model_par.data_path_model_pkl
        with open(model_filename, 'wb') as file:
            pickle.dump(estimator, file)
    else:
        logger.warning("Некорректное имя модели")


if __name__ == '__main__':
    modeling()
