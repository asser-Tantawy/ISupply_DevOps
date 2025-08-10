#!/bin/bash

set -e
#https://github.com/prometheus/node_exporter/releases/download/v1.9.1/node_exporter-1.9.1.linux-arm64.tar.gz
NODE_EXPORTER_VERSION="1.9.1"
ARCH="arm64"  # For AWS Graviton (aarch64)
DOWNLOAD_URL="https://github.com/prometheus/node_exporter/releases/download/v${NODE_EXPORTER_VERSION}/node_exporter-${NODE_EXPORTER_VERSION}.linux-${ARCH}.tar.gz"

echo " Downloading Node Exporter v${NODE_EXPORTER_VERSION} for ${ARCH}..."
wget "$DOWNLOAD_URL"

echo "Extracting ..................."
tar xvf "node_exporter-${NODE_EXPORTER_VERSION}.linux-${ARCH}.tar.gz"

echo "Creating node_exporter user..."
useradd --no-create-home -s /usr/sbin/nologin node_exporter || true

echo "Moving binary to /usr/local/bin..."
cp "node_exporter-${NODE_EXPORTER_VERSION}.linux-${ARCH}/node_exporter" /usr/local/bin/
chown node_exporter:node_exporter /usr/local/bin/node_exporter

echo "Creating systemd service..."
cat <<EOF > /etc/systemd/system/node_exporter.service
[Unit]
Description=Node Exporter
Wants=network-online.target
After=network-online.target

[Service]
User=node_exporter
Group=node_exporter
Type=simple
ExecStart=/usr/local/bin/node_exporter

[Install]
WantedBy=default.target
EOF

echo "Reloading systemd..."
systemctl daemon-reload

echo "Enabling and starting node_exporter..."
systemctl enable node_exporter
systemctl start node_exporter

echo "Node Exporter is running on port 9100"

