sudo snap install multipass

multipass launch --name pkMaster --disk 20G  -m 5G
multipass launch --name pkWorker1 --disk 20G -m 4G
multipass launch --name pkWorker2 --disk 20G -m 2G  

multipass list  
multipass stop pkWorker
multipass delete pkWorker
multipass delete --all
multipass purge

multipass shell pkMaster    
df -h
free -h
multipass shell pkWorker1
multipass shell pkWorker2

sudo passwd ubuntu

sudo apt update && sudo apt upgrade -y && sudo apt install apt-transport-https ca-certificates curl software-properties-common -y && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - && sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" && sudo apt update && sudo apt install docker-ce -y && sudo systemctl start docker && sudo systemctl enable docker && sudo usermod -aG docker ${USER} && sudo su - ${USER} && id -nG && docker --version