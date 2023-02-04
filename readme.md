# Setup
## Make file requirements.txt:
flask  
requests  
mysql-connector-python  

## Run:
pyenv virtualenv 3.8.0 bubble-server  
pyenv activate bubble-server  
pip install --upgrade pip  
pip install -r requirements.txt  

## Setup Mysql database:
* Summary:  
db: tripisdb  
Root user password: kcaFyx6MVu24Bq  
Connection with user: bubble-mysql password: aVMY2std5GYcGX  
* Commands:  
docker run --name bubble-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=kcaFyx6MVu24Bq -d mysql:latest  
- Prima data, dupa crearea contaierului trebuie creat userul cu parola din contigs:  
	CREATE USER 'tripisapp' IDENTIFIED BY 'aVMY2std5GYcGX';  
	GRANT ALL PRIVILEGES ON tripisdb.* TO 'tripisapp';  

- After docker container start, inside the mysql container, create the database:  
	- CREATE DATABASE tripisdb;  

## Connect to local database docker container
docker exec -it bubble-mysql bash  
mysql -u root -p # inside the container  
use tripisdb  

