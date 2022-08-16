# Собрать и запушить образ на гитлаб
docker build -t registry.gitlab.com/uchet.kz/pk/services/elastic ./elastic 
docker push registry.gitlab.com/uchet.kz/pk/services/elastic

# скачать образ
docker pull registry.gitlab.com/uchet.kz/pk/services/elastic:latest

# запустить образ
docker run -p 9200:9200 -e "discovery.type=single-node" registry.gitlab.com/uchet.kz/pk/services/elastic:latest
