ssh af@10.20.30.6 

ssh linux@10.20.30.91
ssh linux@10.20.30.135

ssh pkworker1@10.20.30.91
ssh pkworker2@10.20.30.135

su -l
apt install sudo
apt update
apt install sudo
adduser linux
usermod -aG sudo linux 
ssh linux@10.20.30.135

ssh-copy-id linux@10.20.30.91
ssh-copy-id linux@10.20.30.135