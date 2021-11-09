# Создать контейнер
docker run -it --name mycow --hostname mycow ubuntu bash

# Обновить индексы внутри ubuntu
apt update

# Установить приложение "Корова говорит"
apt install cowsay

# Создать символьную ссылку, чтобы запускать приложение по имени
ln -s /usr/games/cowsay /usr/bin/cowsay

# проверить как работает символьная ссылка 
cowsay "Test"

# После подготовки всех работ на контейнере, можно упаковать его в образ
docker commit mycow doszhanm/cowsay

# Теперь можно из образа создавать контейнеры
docker run doszhanm/cowsay cowsay "Hi"

# Запушить созданный образ в DockerHub
docker push doszhanm/cowsay
Если ошибка по аутентификации, то
docker login