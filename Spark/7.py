from pyspark import SparkConf, SparkContext
  
def breakrecord(rec):
	record = rec.split("|")
	if record[2]=="M":
		return True
	else:
		return False	

con = SparkConf()
sc = SparkContext(conf = con)
rdd1 = sc.textFile("file:///home/cloudera/Desktop/Spark/Users.txt")
rdd2 = rdd1.filter(breakrecord)
data = rdd2.count()
data2 = rdd1.count()
data3 = data2 - data
print "Males:",data
print "Females:", data3
