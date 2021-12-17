docker-compose -f docker-compose-dev.yml up --build

docker exec -it backend_pk_backend_1 bash

./manage.py createsuperuser
./manage.py makemigrations
./manage.py migrate
./manage.py migrate --fake

wsl restart:
Get-Service LxssManager | Restart-Service