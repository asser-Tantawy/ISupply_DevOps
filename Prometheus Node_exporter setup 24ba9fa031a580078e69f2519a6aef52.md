# Prometheus Node_exporter setup

`Node Exporter` It has to be installed on every node you want to monitor.

Get the compatible release from this link : https://github.com/prometheus/node_exporter/releases
copy the link of the release and download it using this link:

```bash
wget https://github.com/prometheus/node_exporter/releases/download/v1.9.1/node_exporter-1.9.1.linux-amd64.tar.gz
```

Then extract it 

```bash
tar -xvf node_exporter-1.9.1.linux-amd64.tar.gz 
```

Then, create a user for this service 

```bash
sudo useradd --no-create-home -s /bin/flase node_exporter
```

Then copy the executable file to the local bin directory 

```bash
cp node_exporter-1.9.1.linux-amd64/node_exporter /usr/local/bin/
#then chage the ownership
chown node_exporter:node_exporter /usr/local/bin/node_exporter 
```

Then you have to create a unit file for it to run it as service 

```bash
sudo vim /etc/systemd/system/node_exporter.service
```

Add this to the file 

```bash
[unit]
Description=Node Exporter
Wants=network-online.target
After=network-online.target

[Service]
User=node_exporter
Group=node_exporter
Type=simple
ExecStart=/usr/local/bin/node_exporter

[Install]
WantedBy=multi-user.target
```

Reload the system daemon to use the service

```bash
sudo systemctl daemon-reload
sudo systemctl start node_exporter
#enable it to run on boot
sudo systemctl enable node_exporter
sudo systemctl status node_exporter # this shoul show running 
```

to verify the service 

```bash
culr -v http://localhost:9100/metrics
```

This should return the server metrics