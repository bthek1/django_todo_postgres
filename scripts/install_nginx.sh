#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

echo "Updating package list..."
sudo apt update

echo "Installing Nginx..."
sudo apt install -y nginx

echo "Nginx installed successfully."
