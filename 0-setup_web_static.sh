#!/usr/bin/env bash
# setup web servers for web_static deployments
apt-get update
apt-get install nginx -y
mkdir -p /data/web_static/{shared,releases/test}
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data
old_content='server_name _;'
new_content='server_name _;\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}'
sed -i "s/$old_content/$new_content/" /etc/nginx/sites-available/default
service nginx --full-restart
