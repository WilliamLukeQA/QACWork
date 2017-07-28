from pyspark import SparkConf, SparkContext, SQLContext, SQLContext
from pyspark.sql.types import *
from pyspark.sql.functions import udf

con = SparkConf()
sc = SparkContext(conf = con)
sql = SQLContext(sc)

def recordsplit(rec):
	record=rec.split("|")
	return record[0],int(record[1])
rdd1 = sc.textFile("file:///home/cloudera/Desktop/Spark/trainee.txt")
head = rdd1.first()
rdd2 = rdd1.filter(lambda line:line != head)
rdd3 = rdd2.map(recordsplit)

def square(a):
	return a*a

def per(a):
	return a*450/100

def outcome(a):
	if a > 1000:
		return "pass"
	else:
		return "fail"

udfper = udf(per,IntegerType())
udfoutcome = udf(outcome,StringType())

schema = StructType([
	StructField('Name', StringType(), True),
	StructField('ID', IntegerType(), True)
	])
df3 = sql.createDataFrame(rdd3, schema)
df3.show()
df3.printSchema()
df3.select('Name',udfper('ID')).show()
df3.select('Name',udfper('ID').alias("per"),udfoutcome(udfper('ID')).alias("outcome")).show()
