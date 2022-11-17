инструкции pritunl:
https://www.youtube.com/watch?v=syn1_R4vTdc&ab_channel=UnixHost
https://computingforgeeks.com/install-pritunl-vpn-on-debian-proxmox-ve/


pritunl
tG47jdCm3PJP

sudo apt install supervisor openvpn -y
sudo systemctl stop openvpn.service
sudo systemctl start openvpn.service
sudo systemctl enable openvpn.service
sudo systemctl status openvpn.service

sudo vim /etc/supervisor/conf.d/openvpn.conf

[program:openvpn]
command=sudo openvpn --config /home/boxroom/programs/openvpn/doszhan_boxroom_doszhan-server.ovpn
autostart=true
autorestart=true


sudo supervisorctl reread   
sudo supervisorctl update
sudo supervisorctl restart all


Освобождение 80 порта:
sudo pritunl set app.redirect_server false
