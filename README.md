## Перед запуском Docker-compose:

Создать в корне файл .env со следующими данными:

POSTGRES_USER=ursip_user

POSTGRES_PASSWORD=qwerty

## Инструкция по запуску:

1) Создать виртуальное Python-окружение
2) Установить зависимости `pip install -r requirements.txt`
3) Создать файл с переменными окружения .env
4) docker-compose up --build
5) файл для парсинга должен находиться в папке /static/parse
5) запустить python файл: src/main.py

### Подключение в Базе данных:

1) psql -h 127.0.0.1 -p 8080 -U ursip_user -d ursip_db

password: qwerty

## После выполнения программы: 
1) должны появиться две таблицы в схеме public: formulars и form_q
2) formulars - таблица, которая содержит название формуляра и его id.
3) form_q - таблица, которая содержит спаршенные данные, которые были предоставлены в формате excel таблице из задания. 
Она содержит так же внешнюю ссылку на таблицу formulars, чтобы проще было внедрять новые формы таблиц из excel для парсинга.


