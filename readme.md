# Fifa21, Filter Engine Third's Api

To start the application you must, build and start the docker containers with the following commands

```
docker-compose build && docker-compose up -d
```

The application will be launched on port 127.0.0.1:8000, it can be configured to run on port 80 to launch production, I recommend adding a ngnix server 

Each start of the containers, will synchronize with the FUT21 api, therefore it will take a while to start, depending on the internet speed



## EndPoints


|       Method         |URL                          |Payload/Args                         |
|----------------|-------------------------------|-----------------------------|
|GET				|`'api/v1/player'`            |/?name={PlayerName}&order={Asc or Desc} #default = asc            |
|POST          |`"api/v1/team"`          	  |{"Name": {TeamName}} |


## AUTH

|       Header         |Key| Type|
|----------------|-------------------------------|-----------------------------|
|x-api-key				|`'API_KEY docker-compose env'`            |string

### Example:
```
environment:
	API_KEY: "key"
build: .
ports:
	- "8000:8000"
depends_on:
	- db
```
