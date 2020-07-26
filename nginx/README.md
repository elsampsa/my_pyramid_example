 
# HTTP and websocket proxy using nginx

- copy file ```pyramid_proxy.conf``` to ```/etc/nginx/conf.d/```
- start websocket server with ```python3 ws_serve.py```
- restart nginx with ```sudo systemctl restart nginx```
- start the webserver with ```pserve --reload dev_nginx.ini```

Now you can access the webpage in http://127.0.0.1:8080 and the websocket example should work

