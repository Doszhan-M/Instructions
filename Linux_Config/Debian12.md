## flathub install
```
https://flatpak.org/setup/Debian
sudo apt install flatpak
sudo apt install gnome-software-plugin-flatpak
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
sudo reboot

flatpak search chrome
flatpak install flathub com.google.Chrome 
```

## Установка расширении:
```
Из менеджера приложении установить Extension Manager

Dash To Panel
AppIndicator and KStatusNotifierItem
Clipboard History
```

## Переключение раскладки клавиатуры:
```
gsettings set org.gnome.desktop.wm.keybindings switch-input-source "['<Shift>Alt_L']"
gsettings set org.gnome.desktop.wm.keybindings switch-input-source-backward "['<Alt>Shift_L']"
```

## Шорткат для терминала:
```
terminal
gnome-terminal
super + T
```

## crow-translate:
```
можно установить из flathub через магазин
```

## Docker:
```
sudo apt update && sudo apt upgrade -y && sudo apt install apt-transport-https ca-certificates curl software-properties-common gnupg -y && curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list  /dev/null && apt-cache policy docker-ce && sudo apt update && sudo apt install docker-ce -y && sudo systemctl start docker && sudo systemctl enable docker && sudo usermod -aG docker ${USER} && sudo su - ${USER} && id -nG && docker --version
```

## docker-compose:
```
https://github.com/docker/compose/tags
export VER="1.29.2" && sudo curl -L "https://github.com/docker/compose/releases/download/${VER}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose && docker-compose --version
```

## zsh:
```
sudo apt -y install zsh
zsh
sudo apt-get install curl -y
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
vim ~/.zshrc 
plugins=(git zsh-autosuggestions zsh-syntax-highlighting)
ZSH_THEME="philips"
reboot pc

Статьи:
  https://habr.com/ru/post/516004/
по умолчанию:
  https://losst.ru/nastrojka-zsh-i-oh-my-zsh
темы отредактировать vi ~/.zshrc:
  https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
Автодополнение:
  https://tehnojam.ru/category/software/oh-my-zsh-autocomlite-like-fish.html
```

## Install solaar:
```
sudo apt update
sudo apt -y install solaar
```

## Изменить локаль на ru:
```
https://unix.stackexchange.com/questions/679315/gnome-debian-11-how-to-install-en-dk-formats-date-numbers-units
  sudo vim /etc/locale.gen
uncomment: ru_RU.UTF-8 UTF-8
  sudo locale-gen
  изменить локали в настройках
```

## openssh-server:
```
sudo apt install openssh-server
sudo systemctl enable ssh
sudo service ssh status 
sudo vi /etc/ssh/sshd_config
port 23
sudo systemctl restart ssh
Если надо отключить:
sudo systemctl disable ssh
```

## grub-settings:
```
  sudo apt update
  sudo apt install grub-customizer -y
  sudo grub-customizer

command for install custom theme:
  cd Programs
  git clone https://github.com/vinceliuice/grub2-themes.git
  sudo ./install.sh -t whitesur -s 2k
  sudo update-grub

если grub не сохраняет последнею загрузку:
  sudo vim  /etc/default/grub 
добавить:
  GRUB_DEFAULT="saved"
  GRUB_SAVEDEFAULT=true
  sudo update-grub  
  GRUB_DISABLE_OS_PROBER=false
  
sudo update-grub
```

## Удалить ненужные программы:
```
sudo apt purge gnome-2048 fcitx kasumi aisleriot atomix gnome-chess five-or-more hitori iagno gnome-klotski lightsoff gnome-mahjongg gnome-mines gnome-nibbles quadrapassel four-in-a-row gnome-robots gnome-sudoku swell-foop tali gnome-taquin gnome-tetravex -y & sudo apt autoremove -y
sudo apt purge xiterm+thai goldendict gnome-contacts gnome-documents hdate-applet uim-gtk2.0 mozc-server mozc-utils-gui mozc-data mlterm malcontent shotwell thunderbird
sudo apt -y purge mlterm-im-skk mlterm-im-uim mlterm-im-wnn mlterm-tiny mlterm-im-canna mlterm-im-scim mlterm-im-m17nlib mlterm-tools mlterm mlterm-im-ibus mlterm-common mlterm-im-fcitx
```

## Install NVIDIA 
```
https://fostips.com/install-nvidia-driver-debian-12/
```

## Символьная ссылка на папку в другом диске:
```
в утилите disks задать auto mount для диска
sudo ln -s /mnt/E2666DE8666DBE43/Store /home/asus/Store
```
