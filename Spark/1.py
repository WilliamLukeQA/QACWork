from pyspark import SparkConf, SparkContext, SQLContext, SQLContext
from pyspark.sql.types import *

con = SparkConf()
sc = SparkContext(conf = con)
sql = SQLContext(sc)

def recordsplit(rec):
	record=rec.split("|")
	return record[0],int(record[1])
rdd1 = sc.textFile("file:///home/cloudera/Desktop/Spark/trainee.txt")
rdd2 = rdd1.map(lambda x:x.split("|"))
head = rdd2.first()
rdd3 = rdd2.filter(lambda line:line != head)
rdd4 = rdd1.map(recordsplit)
df = sql.createDataFrame(rdd3)
df.show()
df.printSchema()
df.select((df._2*100).alias("percentage")).show()
df.filter(df._2 > 500).show()
df.sort(df._2.desc()).show()
df.filter((df._2 > 200) & (df._2 < 500)).show()

df2 = sql.createDataFrame(rdd3, ['Name', 'ID'])
df2.filter(df2.ID > 500).show()

schema = StructType([
	StructField('Name', StringType(), True),
	StructField('ID', LongType(), True)
	])
df3 = sql.createDataFrame(rdd4, schema)
df3.show()
	
