from pyspark import SparkConf, SparkContext

con = SparkConf()
sc = SparkContext(conf = con)

def calculate(x,y):
	personal = x
	result = y
	while result[1][0].
	print result[4][2]
	
rdd1 = sc.textFile("file:///home/cloudera/Desktop/Spark/personal.csv")
rdd2 = sc.textFile("file:///home/cloudera/Desktop/Spark/result.csv")

convert1 = rdd1.map(lambda x: x.encode("ascii","ignore").split(","))
convert2 = rdd2.map(lambda x: x.encode("ascii","ignore").split(","))

data1 = convert1.collect()
data2 = convert2.collect()

pr = calculate(data1,data2)


