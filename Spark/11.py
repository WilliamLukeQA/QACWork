from pyspark import SparkConf, SparkContext

def remove(rec):
	x = rec.split(",")
	return(x[0], x[2])

def add(a,b):
	return int(a)+int(b)

def perc(y):
	y=list(y)
	y[1]=(y[1] * 100 / 300 )
	return y
con = SparkConf()
sc = SparkContext(conf = con)
rdd1 = sc.textFile("file:///home/cloudera/Desktop/Spark/Results.txt")
rdd2 = rdd1.map(lambda x: x.encode("ascii","ignore"))
calc = rdd2.map(remove)
result = calc.reduceByKey(add)
results = result.collect()
per = result.map(perc).collect()

print "Total Marks",results, "Percentage",per
