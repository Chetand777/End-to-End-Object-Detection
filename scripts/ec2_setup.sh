#|bin/bash

sudo apt update

sudo apt-get update

sudo apt upgrade -y

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker $USER

newgrp docker

sudo apt update
sudo apt install python3-venv
python3 -m venv awscli-venv
source awscli-venv/bin/activate
pip install awscli

sudo apt install awscli -y



## AWS Configuration

aws configure


## Now setup elastic IP on AWS