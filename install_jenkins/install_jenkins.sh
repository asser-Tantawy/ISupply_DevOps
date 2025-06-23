#!/bin/bash
sudo apt update
sudo apt install -y openjdk-17-jre-headless

sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins
sudo systemctl enable --now jenkins
echo "now you can access the server at port :8080"
echo "password is :"
cat /var/lib/jenkins/secrets/initialAdminPassword
