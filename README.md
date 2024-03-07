
**Accidents-backend**

1) Create a virtual environment in the root directory.<br>
 ```
python -m venv .venv
```

2) Activate your virtual environment using <br>
```
venv\Scripts\activate
```

3) Pull the docker image for postgres <br>
 ```
docker run -d --name gis -p 5432:5432 -e POSTGRES_PASSWORD=123456789 postgres:14
```

4) Build the docker image of the container using the Dockerfile
```
docker build -t accidents .
```
5) Run the docker-compose.yml file
```
docker-compose up
```
6) Run the server on
```
127.0.0.1:8000
```

