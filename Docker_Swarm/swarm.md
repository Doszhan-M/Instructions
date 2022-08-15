# инициализация swarm на master node
docker swarm init

# присоединить worker ноды
docker swarm join --token SWMTKN-1-1syc7fhxsgkyoot71r2io7x8n5xaxmxulwtcfsovgsf099so6s-761a3k66huuq1yd0bx2mso8y5 10.217.6.191:2377

# список доступных нод
docker node ls

# список сервисов swarm
docker service ls

# деплой docker-stack.yml
docker stack deploy -c docker-stack.yml pk

# лог контейнера
docker service logs -f pk_pgadmin

# данный о контейнере
docker service ps pk_pgadmin