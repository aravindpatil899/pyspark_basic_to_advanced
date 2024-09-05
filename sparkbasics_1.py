from pyspark.sql import SparkSession
#Creation of spark session 
spark = SparkSession.builder.appName("sparkbasics").getOrCreate()
data =[(1,'Aravind','05-11-1994'),(2,'Pradeep','23-09-1994')]
schema  = ['id','name','dob']

df = spark.createDataFrame(data,schema)


df.show()
