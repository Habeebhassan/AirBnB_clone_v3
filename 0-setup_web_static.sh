#!/usr/bin/env bash
# configure web servers for deployment of web_static

echo -e "\e[1;34m BEGIN\e[0m"

# Updates the packages
sudo apt-get -y update
sudo apt-get -y install nginx
echo -e "\e[1;34m Packages updated\e[0m"
echo

# setup firewall
sudo ufw allow 'Nginx HTTP'
echo -e "\e[1;34m Allow incomming NGINX HTTP connections\e[0m"
echo

# create the dir
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo -e "\e[1;34m directories created"
echo

# add test string
echo "<h1>Welcome to www.travol.tech</h1>" > /data/web_static/releases/test/index.html
echo -e "\e[1;34m Test string added\e[0m"
echo

# prevents overwrite
if [ -d "/data/web_static/current" ];
then
    echo "path /data/web_static/current exists"
    sudo rm -rf /data/web_static/current;
fi;
echo -e "\e[1;34m prevent overwrite\e[0m"
echo

# create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data

sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'
echo -e "\e[1;34m Symbolic link created\e[0m"
echo

# restart NGINX
sudo service nginx restart
echo -e "\e[1;34m restart NGINX\e[0m"
