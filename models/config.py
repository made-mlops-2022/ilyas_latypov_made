from dataclasses import dataclass
from typing import List, Dict, Union
from marshmallow_dataclass import class_schema
import yaml


@dataclass
class FeatureParams:
    """
    Feature Parameters
    """
    root_path: str
    data_path_for_modeling: str
    data_path_cat_features: str
    data_path_num_features: str
    data_path_target_path: str
    data_path_ohe_pkl: str
    data_path_scaler_pkl: str
    logging_path: str
    cat_features: List[str]
    num_features: List[str]
    target: str


@dataclass
class ModelParams:
    """
    Model Parameters
    """
    root_path: str
    data_path_cat_features: str
    data_path_num_features: str
    data_path_target_path: str
    data_path_model_pkl: str
    logging_path: str
    target: str
    test_size: float
    model_name: str
    model_param_name: str
    model_param_value: float
    seed: int


@dataclass
class PredictParams:
    """
    Prediction Parameters
    """
    root_path: str
    data_path_for_prediction: str
    target_prediction_path: str
    data_path_ohe_pkl: str
    data_path_scaler_pkl: str
    data_path_model_pkl: str
    logging_path: str
    cat_features: List[str]
    num_features: List[str]
    target: str


def read_config(config_path: str) -> Dict[str, Union[int, float, str]]:
    with open(config_path, "r") as input_stream:
        return yaml.safe_load(input_stream)


def read_config_feature_params(config_path: str) -> FeatureParams:
    params_dict = read_config(config_path)
    report_config_schema = class_schema(FeatureParams)
    config_params = report_config_schema().load(params_dict)
    return config_params


def read_config_model_params(config_path: str) -> ModelParams:
    params_dict = read_config(config_path)
    report_config_schema = class_schema(ModelParams)
    model_params = report_config_schema().load(params_dict)
    return model_params


def read_config_predict_params(config_path: str) -> PredictParams:
    params_dict = read_config(config_path)
    report_config_schema = class_schema(PredictParams)
    predict_params = report_config_schema().load(params_dict)
    return predict_params

# if __name__ == '__main__':
    # path = r"D:/ID/Course/MYENV/HW1_MLOps/ml_project/configs/model_lr/predict.yml"
    # predict_par = read_config_predict_params(path)
    # print(predict_par.num_features)
