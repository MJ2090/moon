# moon
sh setup.sh

source ~/.bashrc

source ~/.DJANGO_SECRET_KEY

// about gunicorn

sudo mkdir -pv /var/{log,run}/gunicorn/

sudo chown -cR ubuntu:ubuntu /var/{log,run}/gunicorn/


// about nginx

sudo vi /etc/nginx/nginx.conf // remove TLSv1 TLSv1.1

sudo vi /etc/nginx/sites-available/moon // copy moon/config/nginx/moon_default

cd /etc/nginx/sites-enabled

sudo ln -s ../sites-available/moon .

sudo systemctl start nginx

sudo systemctl status nginx

// about https

sudo certbot --nginx --rsa-key-size 4096 --no-redirect

sudo vi /etc/nginx/sites-available/moon // something like moon/config/nginx/moon

