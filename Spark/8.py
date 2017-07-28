from pyspark import SparkConf, SparkContext
  
def breakrecord(rec):
	record = rec.split("|")
	return(record[3])

con = SparkConf()
sc = SparkContext(conf = con)
rdd1 = sc.textFile("file:///home/cloudera/Desktop/Spark/Users.txt")

header = rdd1.take(1)[0]
rows = rdd1.filter(lambda line: line != header)

rdd2 = rows.map(breakrecord)
rdd4 = rdd2.distinct().count()
rdd5 = rdd2.countByValue()

print "No. of Job Types",rdd4

for a in rdd5:
	print a,rdd5[a]

