CREATE USER edem_user WITH PASSWORD 'edem_user';

CREATE DATABASE spark_data;
GRANT ALL PRIVILEGES ON DATABASE spark_data TO edem_user;