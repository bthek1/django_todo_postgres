#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

echo "Stopping Todocorn service..."
sudo systemctl stop todocorn

echo "Disabling Todocorn service..."
sudo systemctl disable todocorn

echo "Removing Todocorn service file..."
sudo rm /etc/systemd/system/todocorn.service

echo "Reloading systemd daemon..."
sudo systemctl daemon-reload

echo "Uninstalling Gunicorn..."
poetry remove gunicorn

echo "Gunicorn uninstalled successfully."
