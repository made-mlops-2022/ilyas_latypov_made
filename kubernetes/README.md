## Ilyas Latypov, MADE 2022, MLOps
### HW4 Kubernetes


### Особенности решения
Домашнее задание 2 по online inference я не выполнял
Для выполнения домашнего задания 4 сделал  "заглушку" online-inference:
"docker build -t idlatypov/online-inference:v1 ."
"docker build -t idlatypov/online-inference:v2 ."

Докер заглушка расположена в папке "hello-world-docker"
В нем выполняется одна команда "echo Hello World!" 

Для установки Kubernetes воспользовался встроенным функционалом Docker Desktop (Win10 WSL2). Скрины приложены


### Описание команд
  - "kubectl apply -f online-inference-pod.yaml"                  - Запуск 
  -  "kubectl get pods"          			                            - Проверка статуса pod
  - "kubectl port-forward pods/online-inference 8000:8000"        - Настройка портов


### Project
    ├── hello-world-docker                                        - Docker файлы для "заглушки" online-inference
    │   ├── Dockerfile
    │   └── hello.sh
    ├── Kubernetes_for_WSL2_WIN10.png                    	      - Скриншот установки
    ├── Running Kubernetes.png                                    - Скриншот запуска
    ├── online-inference-pod.yaml                           	  - простой манифест
    ├── online-inference-pod-resources.yaml                 	  - манифест с Requests / Limits
    ├── online-inference-pod-probes.yaml                  	    - манифест запуска с задержкой
    ├── online-inference-replicaset.yaml                         	- манифест с репликами
    ├── online-inference-deployment-blue-green.yaml               - манифест (старые и новые поды есть одновременно)
    ├── online-inference-deployment-rolling-update.yaml           - манифест (с поднятием новых версий, гасятся старые)
    └── README.md                                                 - Description


### Самооценка
+   1. Разверните Kubernetes (5 баллов) - сделано
+   2. Напишите простой Pod manifest для вашего приложения, назовите его online-inference-pod.yaml. Приложите скриншот, где видно, что все поднялось (4 балла) - сделано
+   3. Пропишите Requests / Limits и напишите, зачем это нужно в описании PR. Закоммитьте файл online-inference-pod-resources.yaml (2 балла) - сделано
+   4. Модифицируйте свое приложение так, чтобы оно стартовало не сразу (с задержкой 20-30 секунд) и падало спустя минуты работы (3 балла) - сделано
+   5. Сделайте 3 реплики вашего приложения (3 балла) - сделано
+   6. Опишите [Deployment] для вашего приложения (3 балла) - сделано


+ Итого: 20 баллов
