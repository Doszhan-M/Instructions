# Показать все контейнеры включая остановленные 
docker ps -a

# показать все ранее загруженные образы, не путать с контейнерами
docker images

# Показать все запущенные контейнеры 
docker ps

# Запустить контейнер
docker start heuristic_marquis

# Остановить контейнер 
docker stop heuristic_marquis

# Установить свое имя для запускаемого контейнера 
docker run --name UbuntuNewName -it ubuntu bash

# Флаг -it создать оболочку и войти в него
-it

# Флаг -d запустить в фоновом режиме
docker run -d bitnami/apache

# Запустить на определенном порте, с начало порт на хосте потом порт внутри контейнера
docker run -d -p 8000:8080 bitnami/apache
проверить http://localhost:8000/

# Посмотреть все действия, которые были внутри контейнера
docker logs UbuntuNewName

# Удалить контейнер
docker rm heuristic_marquis

