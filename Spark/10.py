from pyspark import SparkConf, SparkContext
def NewSal(rec):
	return int(rec)+10
con = SparkConf()
sc = SparkContext(conf = con)
rdd1 = sc.textFile("file:///home/cloudera/Desktop/Spark/Money.txt")
rdd2=rdd1.map(lambda x: x.encode("ascii","ignore").split("|"))
newsal = rdd2.mapValues(NewSal)
sal = newsal.collect()
print sal

