from pyspark.sql import SparkSession

spark = SparkSession.builder.master('local').appName('app').getOrCreate()

df = spark.read.csv('file:///home/black/PycharmProjects/pyspark/pyspark_learning/Mall_Customers.csv', header=True,
                    inferSchema=True)
# df.withColumnRenamed('a', 'b')
print(type(df))
print(type(df.toPandas()))
