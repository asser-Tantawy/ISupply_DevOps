# Jenkins instillation

at first you must have java 17 or 21 

```bash
java --version
#output must be 17 or higher 
#if not you must install it using 
apt install openjdk-21-jre-headless
#then check eith java --version
```

if the you still got the wrong version of the java 

```bash
sudo update-alternatives --config java
# you hhave to chosse the right version 
```

then you have to Set JAVA_HOME you add these two lines at ~/.profile  or ~/.bashrc

```bash
export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH
```

then you source the file 

```bash
source .profile
#to test it 
echo $JAVA_HOME
#output /usr/lib/jvm/java-21-openjdk-amd64
```

then you install jenkins 

```bash
sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins
```

after that make sure the service is running and enabled 

```bash
sudo systemctl enable jenkins
sudo systemctl start jenkins
```

 then you run the jenkins UI on port :8080 using [localhost:8080](http://localhost:8080) or serverIP:8080
at the begaing you must put the admin password you get it from 

```bash
cat /var/lib/jenkins/secrets/initialAdminPassword
```

then install the plugins and create admin user done .