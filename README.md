Сервис учёта контейнеров

FastAPI-сервис для управления информацией о контейнерах с использованием MySQL базы данных.
🚀 Технологии

    Backend: FastAPI (Python 3.8+)

    База данных: MySQL 8.0+

    Аутентификация: HTTP Basic Auth

    Документация: Swagger UI / ReDoc

📋 Требования

    Python 3.8+

    MySQL Server или Docker

    pip (менеджер пакетов Python)

🛠️ Установка и запуск
1. Клонирование и настройка окружения
bash

# Создайте виртуальное окружение
python -m venv venv

# Активируйте окружение
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Установите зависимости
pip install -r requirements.txt

2. Настройка базы данных
Вариант A: Запуск с помощью Docker (рекомендуется)
bash

# Запустите MySQL в Docker
docker-compose up -d

# Инициализируйте базу данных
python -m scripts.init_db

# Заполните тестовыми данными
python -m scripts.seed_data

Вариант B: Локальная установка MySQL

    Установите MySQL Server

    Создайте базу данных:
    sql

CREATE DATABASE atk;

    Настройте подключение в файле .env

3. Настройка переменных окружения

Создайте файл .env на основе .env.example:
env

DB_HOST=localhost
DB_PORT=3306
DB_NAME=atk
DB_USER=root
DB_PASSWORD=your_password

Для Docker используйте:
env

DB_HOST=localhost
DB_PORT=3307
DB_NAME=atk
DB_USER=root
DB_PASSWORD=rootpassword

4. Запуск приложения
bash

uvicorn app.main:app --reload

Приложение будет доступно по адресу: http://localhost:8000
📖 Документация API

    Swagger UI: http://localhost:8000/docs

    ReDoc: http://localhost:8000/redoc

🔐 Учетные данные для тестирования

Для доступа к API используйте одного из пользователей:
Логин	Пароль
user1	password1
user2	password2
user3	password3
🚀 Использование API
1. Авторизация

Используйте HTTP Basic Auth с любым из пользователей выше.
2. Доступные endpoints
Поиск контейнеров
text

GET /api/containers?q=ABC

Возвращает контейнеры, номер которых содержит подстроку "ABC"
Поиск по стоимости
text

GET /api/containers/by-cost?min=100&max=500

Возвращает контейнеры в указанном диапазоне стоимости
Добавление контейнера
text

POST /api/containers
{
  "container_number": "ABCU1234567",
  "cost": 250.50
}

Добавляет новый контейнер (номер должен соответствовать формату: 3 буквы + U + 7 цифр)
🐳 Docker Compose

Файл docker-compose.yml содержит конфигурацию для запуска MySQL:
yaml

services:
  mysql:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: atk
      MYSQL_USER: user
      MYSQL_PASSWORD: password
    ports:
      - "3307:3306"
    volumes:
      - mysql_data:/var/lib/mysql

volumes:
  mysql_data:

🔧 Скрипты управления

    scripts/init_db.py - создание базы данных и таблиц

    scripts/seed_data.py - заполнение тестовыми данными

    scripts/clear_data.py - очистка таблиц

🐛 Устранение неполадок
Ошибка подключения к MySQL

    Убедитесь, что MySQL запущен

    Проверьте настройки в файле .env

Ошибка авторизации

    Проверьте правильность логина и пароля

    Убедитесь, что база данных заполнена тестовыми данными

Ошибки валидации

    Номер контейнера должен быть в формате: ABCU1234567 (3 буквы + U + 7 цифр)

    Стоимость должна быть положительным числом

📄 Лицензия

Этот проект создан в рамках тестового задания.
