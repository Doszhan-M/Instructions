# Создать dockerfile

По строкам:

дистрибутив
FROM ubuntu

LABEL Doszhan Develop
описывает кто создал образ

Команда в контейнера
RUN apt-get update && apt-get install -y cowsay && ln -s /usr/games/cowsay /usr/bin/cowsay

Точка входа внутри контейнера
ENTRYPOINT [ "cowsay" ]

# Создать образ по dockerfile
docker build -t doszhanm/cowsay2 .

# Теперь можно создать контейнер из этого образа
docker run doszhanm/cowsay2 "Hello"