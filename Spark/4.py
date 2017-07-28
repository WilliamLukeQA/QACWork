from pyspark import SparkConf, SparkContext

con = SparkConf()
sc = SparkContext(conf = con)

list = [1,2,3,4,5,6,7,8,4,3,5,3,5,7,3,2,5,5,4]
rdd1 = sc.parallelize(list)
num = rdd1.count()
data = rdd1.countByValue()

for k in data:
	print(k,"-",data[k])
