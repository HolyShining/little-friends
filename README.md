# Little friends

# Запуск проекту

- Для початку потрібно створити пусту базу даних для проекту, в БД `postgres` введіть команду

```
CREATE DATABASE little_friends;
```

- Далі потрібно налаштувати віртуальне оточення:

  - Для запуску віртуального оточення через `poetry`:

  ```
  poetry install
  poetry shell
  ```

  - Для запуску через `virtualenv`:

  ```
  python3 -m venv /venv_friends
  source venv_friends/bin/activate
  pip install -r requirements.txt
  ```

- Далі заповніть `.env` файл:

```
touch .env
echo DATABASE_URL=postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@$localhost:5432/little_friends >> .env
echo SECRET_KEY=$(openssl rand -hex 32) >> .env
```

- Для запуску додатку (в режимі розробника):

```
alembic upgrade head
uvicorn app.main:app --reload
```

# Запуск додатку за допомогою 'Docker'

- Встановіть `docker` та `docker-compose`

- Заповніть .env файл:

```
touch .env
echo DB_CONNECTION=postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB >> .env
echo SECRET_KEY=$(openssl rand -hex 32) >> .env
```

- Запустіть базу даних та додаток

```
docker-compose up
```

# Структура проекту

```
    app
    ├── api              - обробники AJAX запитів
    ├── controllers      - обробники для сторінок проекту
    ├── core             - Системні налаштування серверу (логування, конфігурація, обробники подій)
    ├── db               - Нижній рівень роботи з бд (міграції та репозиторії)
    ├── models           - Типізовані моделі з бд для роботи pydantic
    ├── resources        - Константи, які використовуються у проекті
    ├── services         - Логіка, яка не відноситься до CRUD операцій
    ├── static           - Статичні файли серверу (картинки, CSS, JS файли)
    ├── templates        - HTML/Jinja2 шаблони сторінок, які віддаються кінцевому користувачу
    └── main.py          - Створення ASGI додатку з усіма конфігураціями
```
