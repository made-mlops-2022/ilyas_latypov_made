import sys
sys.path.append(".")
import pickle
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from ml_project.models.config import read_config_feature_params
from ml_project.models.logger import start_logger, create_parser


def features_prepare(arg1=None):
    parser = create_parser(arg1)
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.arg1 is None:
        print("Specify the config file as а parameter")
        return

    feat_par = read_config_feature_params(namespace.arg1)
    logger = start_logger(feat_par.root_path + feat_par.logging_path)
    logger.info("Инициализация логирования и загрузка файла параметров")

    logger.debug("Загрузка данных")
    data = pd.read_csv(feat_par.root_path + feat_par.data_path_for_modeling)
    logger.debug("Сохранение target")
    data[[feat_par.target]].to_csv(feat_par.root_path + feat_par.data_path_target_path,
                                   index=False)

    logger.debug("Расчет и сохранение StandardScaler для числовых признаков")
    scaler = StandardScaler()
    x_num = scaler.fit_transform(data[feat_par.num_features].values)
    df_num = pd.DataFrame(x_num, columns=feat_par.num_features)
    df_num.to_csv(feat_par.root_path + feat_par.data_path_num_features, index=False)

    logger.debug("Сохранение модели(pkl) StandardScaler для числовых признаков")
    scaler_filename = feat_par.root_path + feat_par.data_path_scaler_pkl
    with open(scaler_filename, 'wb') as file:
        pickle.dump(scaler, file)

    logger.debug("Расчет и сохранение OneHotEncoder для категориальных признаков")
    ohe = OneHotEncoder(handle_unknown='ignore')
    ohe.fit(data[feat_par.cat_features])
    x_cat = ohe.transform(data[feat_par.cat_features]).toarray()

    columns_ = []
    for idx_j in range(len(ohe.categories_)):
        for idx_i in range(len(ohe.categories_[idx_j])):
            columns_.append(feat_par.cat_features[idx_j] + "_ohe" + str(idx_i))

    df_cat = pd.DataFrame(x_cat, columns=columns_)
    df_cat.to_csv(feat_par.root_path + feat_par.data_path_cat_features, index=False)

    logger.debug("Сохранение модели(pkl) OneHotEncoder для категориальных признаков")
    ohe_filename = feat_par.root_path + feat_par.data_path_ohe_pkl
    with open(ohe_filename, 'wb') as file:
        pickle.dump(ohe, file)

    return x_num, x_cat, data[[feat_par.target]]


if __name__ == '__main__':
    features_prepare()
