# Shape data challenge
### Necessary to run the project
To run this project is necessary to have docker and docker-compose

Links to install:
* Docker: https://docs.docker.com/install/linux/docker-ce/ubuntu/
* Docker-compose: https://docs.docker.com/compose/install/

### Necessary to populate the DB
To populate the DB is necessary to have psycopg2 and pandas
 * Command to install it: pip3 install pandas psycopg2
 
### Running the project
The docker will create the DB and up the project

* Command to run: docker-compose up

As all is executed the DB will be created and the project will be running

After that in the first you run is necessary to populate DB.
At the scripts file has a script that populate the DB.
* Command to run the script: python3 insert_data.py

### Executing the endpoints
To execute the endpoints is possible to use the documentation of swagger.
For that with the project running access: http://localhost:5000/apidocs/
