инструкции pritunl:
https://www.youtube.com/watch?v=syn1_R4vTdc&ab_channel=UnixHost
https://computingforgeeks.com/install-pritunl-vpn-on-debian-proxmox-ve/


0d3006e55e8541528f88da75f9345a09

pritunl
Mu61cv@^i7KU


sudo apt install openvpn -y
sudo systemctl stop openvpn.service
sudo systemctl start openvpn.service
sudo systemctl status openvpn.service

sudo vim /etc/supervisor/conf.d/openvpn.conf

[program:openvpn]
command=sudo openvpn --config /home/boxroom/programs/ovpn/vpn_org_boxroom_google_vpn.ovpn
user=boxroom
process_name=%(program_name)s
numprocs=1
autostart=true
autorestart=true
redirect_stderr=true

sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl
