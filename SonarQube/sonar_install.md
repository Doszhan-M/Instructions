### manual:
https://derryberni.medium.com/how-to-setup-sonar-cube-sonar-scanner-with-docker-compose-simple-15c9d84966dc

## max virtual memory config:
sudo vim /etc/sysctl.conf
add: </br>
```vm.max_map_count=262144```


## zsh path config:
vim ~/.zshrc 
add: 
</br>
export PATH=$PATH:/home/asus/Programs/sonar-scanner-4.7/bin


### test credentials:
admin:4fXGqRHTAasUfpMh
