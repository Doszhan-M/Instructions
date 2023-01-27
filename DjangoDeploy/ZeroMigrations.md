1. ВАЖНО! С начало проверить, чтобы на всех серверах были применены текущие миграции.
python3 manage.py makemigrations
2. Забекапить все текущие миграции
3. Через pgAdmin забекапить таблицу django_migrations
4. Через pgAdmin очистить все записи на таблице django_migrations
5. Выполнить python3 manage.py makemigrations (если выходит ошибка ValueError: Dependency on app with no migrations, необходимо чтобы в проекте не было папок migrations)
6. Выполнить команду python3 manage.py migrate --fake
7. Через pgAdmin проверить таблицу django_migrations, если все миграции записались, можно удалять старые миграции


Также есть вариант через команду python manage.py migrate --fake accounts zero
