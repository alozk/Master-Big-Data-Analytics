<h1>Kafka - Docker - PostgreSQL</h1>

Steps to run:

1) docker compose build
2) docker compose up -d
3) Navigate to localhost:8080 and check topic mock_data exist if not create
4) Execute the following command:
```
docker exec spark-master /opt/spark/bin/spark-submit --master spark://spark-master:7077 --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.2,org.postgresql:postgresql:9.4.1207 --driver-memory 1G --executor-memory 1G /opt/spark-apps/main.py
```

Use any PostgreSQL client to check the database, i.e. [DBeaver](https://dbeaver.io/). Database name and credentials are in [init.sql](postgresql/init.sql)