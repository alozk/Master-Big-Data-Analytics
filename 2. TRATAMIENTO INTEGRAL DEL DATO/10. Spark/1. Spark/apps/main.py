import os
from tkinter.dnd import dnd_start
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

schema = StructType(
        [
                StructField("id", StringType()),
                StructField("name", StringType()),
                StructField("last_name", StringType()),
                StructField("friends", ArrayType(StringType())),
                StructField("position", StructType([
                    StructField("lat", StringType()),
                    StructField("lon", StringType())
                ])),
                StructField("transport", StringType()),
                StructField("age", StringType()),
                StructField("gender", StringType()),
                StructField("weight", StringType()),
                StructField("height", StringType()),
                StructField("bodyfat", StringType()),
                StructField("bloodpressure_sist", StringType()),
                StructField("bloodpressure_diast", StringType()),
                StructField("cholesterol", StringType()),
                StructField("smoker", StringType()),
                StructField("drinking", StringType()),
                StructField("disability", StringType()),
                StructField("previouspatology", StringType()),
                StructField("cp", StringType()),
                StructField("time", StringType())
        ]
)

def init_spark():
    print("Creating session")
    spark = SparkSession.builder.appName("EDEM_APP").getOrCreate()
    spark.sparkContext.setLogLevel('WARN')
    return spark

def postgres_sink(table_dst, df):
    dbname = "spark_data"
    dbuser = "edem_user"
    dbpass = "edem_user"
    dbhost = "db"
    dbport = "5432"

    url = "jdbc:postgresql://"+dbhost+":"+dbport+"/"+dbname
    properties = {
        "driver": "org.postgresql.Driver",
        "user": dbuser,
        "password": dbpass
    }

    df.write.jdbc(url=url, table=table_dst, mode="append",
                          properties=properties)


def doThings(df):
    pass

def writeToSQLWarehouse(df, epochId):
    pass


def main():
    spark=init_spark()
    stream_detail_df = spark.readStream.format("kafka")\
                    .option("kafka.bootstrap.servers", "kafka0:29092")\
                    .option("subscribe", "mocked_data")\
                    .option("startingOffsets", "earliest")\
                    .load()

    #stream_detail_df.printSchema()
    ds = stream_detail_df.selectExpr("CAST(value AS STRING)")

if __name__ == '__main__':
  main()