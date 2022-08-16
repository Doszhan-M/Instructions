# Собрать и запушить образ на гитлаб
docker build -t registry.gitlab.com/uchet.kz/pk/services/elastic ./elastic 
docker push registry.gitlab.com/uchet.kz/pk/services/elastic

# скачать образ
docker pull registry.gitlab.com/uchet.kz/pk/services/elastic:latest