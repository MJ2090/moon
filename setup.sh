#!/bin/sh
echo "ALL started ================================="
sudo apt update
sudo apt install python3-pip -y
sudo apt install mlocate -y
pip install gradio
pip install wandb
pip install django
pip install gunicorn
pip install torch==2.0.0
pip install tensorboardX==2.6
pip install bitsandbytes==0.37.2
pip install accelerate==0.18.0
pip install fire==0.5.0
pip install git+https://github.com/huggingface/peft.git
sudo apt install nginx -y

echo 'alias gl="git pull"' >> ~/.bashrc
echo 'alias dr="python3 manage.py runserver 0.0.0.0:8000"' >> ~/.bashrc
echo 'alias p3="python3"' >> ~/.bashrc
echo 'alias dc="python3 manage.py collectstatic"' >> ~/.bashrc
echo 'alias gk="pkill gunicorn"' >> ~/.bashrc
echo 'alias gs="gunicorn -c config/gunicorn/prod.py"' >> ~/.bashrc

sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot

echo "ALL ended ================================="
