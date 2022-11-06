## Ilyas Latypov, MADE 2022, MLOps
### HW1 "production ready" проект

### Краткое описание проекта (архитектурные и тактические решения)

Исходные данные для построения модели https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci

Для предобработки данных используется:
 - StandardScaler для числовых признаков
 - OneHotEncoding для категориальных признаков 

Для классификации используются две модели:
 - Logistic Regression
 - KNeighborsClassifier

Сделанo EDA в блокноте (.ipynb)  - опеределены значения гиперпараметров
Cделан скрипт отчета EDA по исходным данным
Скрипты запускаются с командной строки, которые принимают на вход файлы конфигурации

### Описание команд
 - "python reports/report.py"                                                            - Построение отчета по исходным данным
 -  "pytest ../tests --cov"                                                                    - тестирование проекта из папки models
Для модели Logistic Regression
 - "python models/features.py configs/model_lr/features.yml"       - расчет признаков и сохранение моделей OneHotEncoding и StandardScaler 
 - "python models/modeling.py configs/model_lr/modeling.yml"   - настройка и сохранение модели Logistic Regression (расчет метрик train и test)
 - "python models/prediction.py configs/model_lr/predict.yml"      - применение сохраненных моделей на новых данных, расчет прогноза
Для модели KNeighborsClassifier
 - "python models/features.py configs/model_kn/features.yml"       - расчет признаков и сохранение моделей OneHotEncoding и StandardScaler 
 - "python models/modeling.py configs/model_kn/modeling.yml"   - настройка и сохранение модели KNeighborsClassifier (расчет метрик train и test)
 - "python models/prediction.py configs/model_kn/predict.yml"      - применение сохраненных моделей на новых данных, расчет прогноза

Обученные модели сохраняются в папке models_pkl
Для предсказания используется входной файл data_for_prediction\data\data_sample.csv
Предсказания записываются в data_for_prediction\prediction\

### Project

    ├── configs                            - Config files
    │   ├── model_kn                          - Config files for KNeighborsClassifier model
    │   │   ├── features.yml                     - Config file for features generation
    │   │   ├── modeling.yml                     - Config file for modeling
    │   │   └── predict.yml                      - Config file for prediction
    │   └── model_lr                          - Config files for LogisticRegression model
    │        ├── features.yml                    - Config file for features generation
    │        ├── modeling.yml                    - Config file for modeling
    │        └── predict.yml                     - Config file for prediction
    │
    ├── data_for_modeling                  - Data for modeling
    │   ├── data                              - Original dataset
    │   │   ├── heart_cleveland_upload.csv
    │   │   └── data_description.txt
    │   └── features                          - Dataset for modeling (Features + Target)                 
    │        ├── model_kn                        - Features for KNeighborsClassifier model
    │        │   ├── cat_features.csv               - категориальные признаки
    │        │   ├── num_features.csv               - числовые признаки
    │        │   └── target.csv                     - целевой признак
    │        └── model_lr                        - Features for LogisticRegression model
    │             ├── cat_features.csv              - категориальные признаки
    │             ├── num_features.csv              - числовыепризнаки
    │             └── target.csv                    - целевой признак
    │
    ├── data_for_prediction                - Data for prediction
    │   ├── data                              - Datasets for predictions
    │   │   ├── data_sample.csv
    │   │   └── data_synt_sample.csv
    │   └── prediction                        - Predictions of models
    │        ├── prediction_kn.csv               - Predictions for KNeighborsClassifier model
    │        └── prediction_lr.csv               - Predictions for LogisticRegression model
    │
    ├── logs                              - Logs
    │   ├── logging_model_kn.log             - Logging for KNeighborsClassifier model
    │   └── logging_model_lr.log             - Logging for LogisticRegression model
    │
    ├── models                            - Source codes
    │   ├── configs.py                       - Code for config loading   
    │   ├── features.py                      - Code for data preparing and features generation       
    │   ├── logger.py                        - Code for logging preparation       
    │   ├── modeling.py                      - Code for models(pkl) generation
    │   ├── prediction.py                    - Code for target prediction
    │   └── prepare_sample                   - Code for synthetic data generation
    │
    ├── models_pkl                        - Trained models(pkl)
    │   ├── model_kn                         - Trained models(pkl) for KNeighborsClassifier 
    │   │   ├── ohe.pkl                         - OneHotEncoding saved model (pkl) 
    │   │   ├── scaler.pkl                      - StandardScaler saved model (pkl)
    │   │   └── kn_clf.pkl                      - KNeighborsClassifier saved model (pkl)
    │   └── model_lr                         - Trained models(pkl) for LogisticRegression 
    │        ├── ohe.pkl                        - OneHotEncoding saved model (pkl) 
    │        ├── scaler.pkl                     - StandardScaler saved model (pkl)
    │        └── log_reg.pkl                    - LogisticRegression saved model (pkl) 
    │
    ├── notebooks                         - Jupyter notebook with EDA 
    │   ├── EDA.ipynb                        - Jupyter notebook with EDA (.ipynb format)
    │   └── EDA.html                         - Jupyter notebook with EDA (.html format)
    │
    ├── reports                           - Code for EDA report and report file
    │   ├── report.py                        - Code for EDA report
    │   └── report.html                      - Report file
    │
    ├── tests                             - PyTest code (for features, modeling, predictions, pipeline, synthetic data)
    │   ├── test_features_modeling.py
    │   ├── test_modeling.py
    │   ├── test_pipeline.py
    │   └── test_synt_data.py
    │
    ├── README.md                         - Description
    │
    └── requirements.txt                  - Requirements

### Самооценка
Ветка для проекта homework1, код в папке ml_project:
+   0. В описании к пулл-реквесту описаны основные "архитектурные" и тактические решения, которые сделаны в вашей работе (1 балл) - сделано
+   1. В пулл-реквесте проведена самооценка (1 балл) - сделано
+   2. Выполнение EDA, закоммитьте ноутбук в папку с ноутбуками (1 балл) - сделано
+   2. Написать скрипт, который сгенерит отчет, закоммитьте и скрипт и отчет (1 балл) - сделано
+   3. Написана функция для тренировки модели, вызов оформлен как утилита командной строки, записана в readme инструкцию по запуску (3 балла) - сделано
+   4. Написана функция predict (вызов оформлен как утилита командной строки), запишет предикт по заданному пути, инструкция по вызову записана в readme (3 балла) - сделано
+   5. Проект имеет модульную структуру (2 балла) - сделано
+   6. Использованы логгеры (2 балла) - сделано
+   7. Написаны тесты на отдельные модули и на прогон обучения и predict (3 балла) - сделано
+   8. Для тестов генерируются синтетические данные, приближенные к реальным (2 балла)  - сделано
+   9. Обучение модели конфигурируется с помощью конфигов в json или yaml, закоммитьте 2 корректные конфигурации, с помощью которых можно обучить модель (3 балла) - сделано
+ 10. Используются датаклассы для сущностей из конфига, а не голые dict (2 балла) - сделано
-  11. Напишите кастомный трансформер и протестируйте его (3 балла) - не сделано
+ 12. В проекте зафиксированы все зависимости (1 балл) - сделано
-  13. Настроен CI для прогона тестов, линтера на основе github actions (3 балла) - не сделано

+ Итого: 25 баллов
