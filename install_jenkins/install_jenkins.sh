#!/bin/bash
#install java
sudo apt update
sudo apt install -y openjdk-21-jre-headless
#add java to the user path
echo "export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64" >> ~/.profile
echo "export PATH=$JAVA_HOME/bin:$PATH" >> ~/.profile
source ~/.profile

# install jenkins
sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins

#install Docker
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
#enable jenkins 
sudo systemctl enable --now jenkins
# add jenkins and user to docker group
sudo usermod -aG docker jenkins
sudo usermod -aG docker $USER 
#print initial password
echo "now you can access the server at port :8080"
echo "password is :"
cat /var/lib/jenkins/secrets/initialAdminPassword
