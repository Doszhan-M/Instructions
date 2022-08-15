# инициализация swarm на master node
docker swarm init

# список сервисов swarm
docker service ls

# список доступных нод
docker node ls

# присоединить worker ноды
docker swarm join --token SWMTKN-1-69nzfscisrpszxvotwjor1cn4n5uxk63wy6zbpopgff5dk0pm1-2ue3awirwxxljjtyjnt9o0rjq 10.217.6.191:2377

# список доступных нод
docker node ls
