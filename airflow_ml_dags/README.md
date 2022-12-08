## Ilyas Latypov, MADE 2022, MLOps
### HW3 AirFlow

### Описание команд
 - "docker-compose up --build"                                                              - Запуск AirFlow
 -  "pytest -v tests/"                                                                                - Запуск тестов

### Project
    ├── dags                                                                                             - python dag files
    ├── images                                                                                         - image files
    ├── screens                                                                                        - Airflow screenshots
    ├── test                                                                                               - python file for pytest
    ├── docker-compose.yml                                                                    - docker file
    └── README.md                                                                                 - description


### Самооценка
Ветка для проекта homework1, код в папке ml_project:
+   0. Поднимите airflow локально, используя `docker compose` (можно использовать из примера https://github.com/made-ml-in-prod-2021/airflow-examples/) (0 баллов) - сделано
+   1. Реализуйте dag, который генерирует данные для обучения модели. Вам важно проэмулировать ситуации постоянно поступающих данных  (5 баллов) - сделано
+   2. Реализуйте dag, который обучает модель еженедельно, используя данные за текущий день. В вашем пайплайне должно быть как минимум 4 стадии (10 балл) - сделано
+   3. Реализуйте dag, который использует модель ежедневно (5 баллов) - сделано
+   4. Использовать `DockerOperator` -- тогда выполнение каждой из тасок должно запускаться в собственном контейнере. Все даги реализованы только с помощью `DockerOperator` (10 баллов) - сделано
+   5. Самооценка (1 балл) - сделано
+   6. Реализуйте сенсоры на то, что данные готовы для дагов тренировки и обучения (+3 доп балла)  - сделано
+   7. Протестируйте ваши даги https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html (+5 доп баллов)  - сделано
+   10. Настройте alert в случае падения дага https://www.astronomer.io/guides/error-notifications-in-airflow (+3 доп балла) - сделано

+ Итого: 42*0.6 = 25 баллов
