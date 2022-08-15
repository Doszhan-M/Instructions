# Цель - соединить 2 контейнера база данных mariadb и управляющая консол adminer

# Установить mariadb, найти ее на dockerhub
docker run --detach --name mysqlserver --env MARIADB_USER=example-user --env MARIADB_PASSWORD=my_cool_secret --env MARIADB_ROOT_PASSWORD=my-secret-pw  mariadb:latest

# Проверить работает ли сервер
docker ps

# Установить adminer, найти ее на dockerhub
docker run --link mysqlserver:db -p 8080:8080 adminer
тут флаг --link соединяет 2 контейнера mysqlserver и adminer

# Проверяем работу сервера и админера
http://localhost:8080/

# Произмвести вход
логин -- example-user
пароль -- my_cool_secret