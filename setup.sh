#!/bin/sh
echo "ALL started ================================="

sudo apt install python3-pip -y
pip install django
pip install gunicorn
sudo apt install nginx -y

echo 'alias gl="git pull"' >> ~/.bashrc
echo 'alias dr="python3 manage.py runserver 0.0.0.0:8000"' >> ~/.bashrc
echo 'alias p3="python3"' >> ~/.bashrc
echo 'alias dc="python3 manage.py collectstatic"' >> ~/.bashrc
echo 'alias gk="pkill gunicorn"' >> ~/.bashrc
echo 'alias gs="gunicorn -c config/gunicorn/prod.py"' >> ~/.bashrc

echo "ALL ended ================================="