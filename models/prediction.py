import sys
sys.path.append(".")
import pickle
import pandas as pd
import numpy as np
from ml_project.models.config import read_config_predict_params
from ml_project.models.logger import start_logger, create_parser


def prediction(arg1=None):
    parser = create_parser(arg1)
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.arg1 is None:
        print("Specify the config file as а parameter")
        return

    predict_par = read_config_predict_params(namespace.arg1)
    logger = start_logger(predict_par.root_path + predict_par.logging_path)
    logger.info("Инициализация логирования и загрузка файла параметров")

    logger.debug("Загрузка данных")
    data_path = predict_par.root_path + predict_par.data_path_for_prediction
    data = pd.read_csv(data_path)

    logger.debug("Загрузка OneHotEncoder и применение для категориальных признаков")
    ohe_filename = predict_par.root_path + predict_par.data_path_ohe_pkl
    with open(ohe_filename, 'rb') as file:
        ohe = pickle.load(file)
    x_cat = ohe.transform(data[predict_par.cat_features]).toarray()

    logger.debug("Загрузка StandardScaler и применение для числовых признаков")
    scaler_filename = predict_par.root_path + predict_par.data_path_scaler_pkl
    with open(scaler_filename, 'rb') as file:
        scaler = pickle.load(file)
    x_num = scaler.fit_transform(data[predict_par.num_features].values)
    x_num_cat = np.hstack((x_num, x_cat))

    logger.debug("Загрузка и применение модели")
    model_filename = predict_par.root_path + predict_par.data_path_model_pkl
    with open(model_filename, 'rb') as file:
        estimator = pickle.load(file)
    y_pred = estimator.predict(x_num_cat)
    target_pred_path = predict_par.root_path + predict_par.target_prediction_path
    predict_target = pd.DataFrame(y_pred, columns=[predict_par.target])
    predict_target.to_csv(target_pred_path, index=False)
    return predict_target


if __name__ == '__main__':
    prediction()
