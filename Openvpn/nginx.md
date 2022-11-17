sudo wget https://nginx.org/keys/nginx_signing.key
sudo apt update
sudo apt install -y gnupg2
sudo apt-key add nginx_signing.key
sudo apt update
sudo apt install -y nginx
sudo systemctl start nginx
sudo systemctl enable nginx


## Nginx Config:

Отредактировать файл default:
sudo vim /etc/nginx/sites-enabled/
Все удалить (ggVG) и вставить:

server {
    server_name  doszhan.online www.doszhan.online;

    client_max_body_size 100M;

    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;

    location / {
        proxy_pass http://192.168.221.2;
        proxy_redirect off;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        }

}

sudo nginx -t
sudo service nginx status
sudo service nginx start
sudo service nginx stop

## certbot
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d doszhan.online -d www.doszhan.online

