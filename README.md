# Hello World Applications with Reverse Proxy
Run hello world applications from many languages with Nginx as Reverse Proxy.

## Author
* Michael Susanto

## Techstacks
- Django (Web Server)
- Flask (Web Server)
- Go (Web Server)
- NodeJS (Web Server)
- Nginx (Reverse Proxy)

## How to use
* Run & build the services
```cmd
docker-compose up -d --build
```

* Stop the service
```cmd
docker-compose down -v
```

## Routes:
- Django -> http://localhost/django/
- Flask -> http://localhost/flask/
- Go -> http://localhost/go/
- NodeJS -> http://localhost/node/