# Ilyas Latypov, MADE 2022, MLOps
### HW1 "production ready" проект


### Project

    ├── configs                       - Config files.
    │
    ├── data_for_modeling
    │   ├── data                       - Original dataset
    │   └── features                 - Dataset for modeling (Features + Target)                 
    │
    ├── data_for_prediction
    │   ├── data                       - Dataset for predictions
    │   └── prediction              - Predictions of models
    │
    ├── logs                            - Logs
    │
    ├── models            
    │   ├── configs.py             - Code for config loading   
    │   ├── features.py            - Code for data preparing and features generation       
    │   ├── modeling.py          - Code for models(pkl) generation
    │   ├── prediction.py         - Code for target prediction
    │
    ├── models_pkl                - Trained models(pkl)
    │
    ├── notebooks                  - Jupyter notebook with EDA
    │
    ├── reports                       - Code for EDA report and report-file
    │
    ├── tests                           - PyTest code
    │
    ├── README.md              - Description
    │
    ├── requirements.txt        - Requirements