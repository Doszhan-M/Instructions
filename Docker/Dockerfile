FROM ubuntu 

LABEL Doszhan Develop

RUN apt-get update && apt-get install -y cowsay && ln -s /usr/games/cowsay /usr/bin/cowsay

ENTRYPOINT [ "cowsay" ]