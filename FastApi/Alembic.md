# 1. В корне выполнить 
alembic init migrations

# 2. В alembic.ini прописать путь до базы
sqlalchemy.url = postgresql://fastapi:fastapi@localhost/fastapi_db

# 3. В env.py импортировать SQLALCHEMY_DATABASE_URL и Base
from database.database import SQLALCHEMY_DATABASE_URL
from database.base import Base

# 4. Изменить target_metadata
target_metadata = Base.metadata

# 5. Создать миграции
alembic revision --autogenerate -m "First"

# 6. Выполнить миграции
alembic upgrade head

# 7. Проверить базу через pgadmin 