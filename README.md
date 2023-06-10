## how to run this project

sudo docker-compose build
sudo docker-compose up 

## how to reach mongodb
sudo docker exec -it mongodb bash

mongosh --host localhost --port 27017 -u admin -p password --authenticationDatabase admin