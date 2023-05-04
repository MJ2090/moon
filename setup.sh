#!/bin/sh
echo "ALL started ================================="

sudo apt install python3-pip -y
pip install django
pip install gunicorn
sudo apt install nginx

echo "ALL ended ================================="