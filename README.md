# Тестовое задание

![image](https://github.com/user-attachments/assets/de9feb0f-fe61-4f76-aec4-62d5f9dd80ee)

# Описание решения
Решение было реализовано на Flask. Добавлена визуализация работы в html. Приложение завернуто в Docker. Для корректной загрузки Elasticsearch и создания индекса была реализована система ожидания.

## Технологический стек
    Python(Flask, pandas)
    Elasticsearch
    Docker    

### Библиотеки
    Flask==3.0.3
    Pandas==2.2.2
    Elasticsearch==8.15.0

## Развертка проекта(может понадобится VPN)
    git clone https://github.com/EgorZhizhlo/Task.git
    cd Task
    docker-compose up --build

## URLS
    / - основная страница с полем для ввода текста для поиска и удаления
    search/ - страница вывода результата поиска согласно ТЗ
    delete/ - страница удаления записи по id согласно ТЗ
