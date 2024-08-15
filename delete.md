server {
listen 80;
server_name 140.238.195.138;

location = /favicon.ico { access_log off; log_not_found off; }
location /static/ {
root /home/ubuntu/Testing/django_todo;
}

location / {
include proxy_params;
proxy_pass http://unix:/home/ubuntu/Testing/django_todo/gunicorn.sock;
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
}
}
