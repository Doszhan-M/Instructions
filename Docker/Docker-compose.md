# Собрать и поднять docker-compose флаг -d запустить в фоновом режиме
docker-compose up -d

# Посмотреть все активные docker-compose
docker-compose ps

# Остановить все docker-compose 
docker-compose stop

# Остановить все docker-compose и удалить контейнеры, флаг -v удалить также созданные тома локально
docker-compose down -v 
