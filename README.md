# moon
sh setup.sh

source ~/.bashrc

source ~/.DJANGO_SECRET_KEY

sudo mkdir -pv /var/{log,run}/gunicorn/

sudo chown -cR ubuntu:ubuntu /var/{log,run}/gunicorn/

