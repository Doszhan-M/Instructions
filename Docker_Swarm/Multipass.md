multipass launch --name pkMaster
multipass launch --name pkWorker1
multipass launch --name pkWorker2

multipass list
multipass stop pkWorker2
multipass delete pkWorker2
multipass purge

multipass shell pkMaster
multipass shell pkWorker1
multipass shell pkWorker2


sudo apt update && sudo apt upgrade -y && sudo apt install apt-transport-https ca-certificates curl software-properties-common -y && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - && sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" && sudo apt update && sudo apt install docker-ce -y && sudo systemctl start docker && sudo systemctl enable docker && sudo usermod -aG docker ${USER} && sudo su - ${USER} && id -nG && docker --version

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose && docker-compose --version