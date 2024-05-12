#|bin/bash

sudo apt update

sudo apt install openjdk-8-jdk -y

https://pkg.jenkins.io/
https://pkg.jenkins.io/debian-stable/

sudo systemctl start jenkins

sudo systemctl enable jenkins

sudo systemctl status jenkins



## Instaling Docker

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker $USER

sudo usermod -aG docker jenkins


newgrp docker

sudo apt update
sudo apt install python3-venv
python3 -m venv awscli-venv
source awscli-venv/bin/activate
pip install awscli


sudo apt install awscli -y

sudo usermod -a -G docker jenkins


## AWS Configuration and restarts jenkins

aws configure


## Setup elastic IP on AWS



## For getting admin password for jenkins

sudo cat /var/lib/jenkins/secrets/initialAdminPassword