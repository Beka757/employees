# Online Catalog

## Запуск проекта на Django
#### Создайте базе данных в Postgres
    Укажите название бд "test_db"
    Укажите пользователя "test_user"
    Укажите пароль для пользователя "test_password"
#### Установите виртуальное окружение
    python3 -m venv venv
#### Активируйте виртуальное окружение
    source venv/bin/activate
#### Установите зависимости
    pip install -r requirements.txt
#### Произведедите миграцию
    python3 manage.py migrate
#### Запустите скрипт "seed.sh" для тестового заполнения данных(50000 данных!!!! Можете сменить настройки)
#### Запустите проект
    python3 manage.py runserver
#### Для проверки API запросов
    Перейти api/swagger/ 
