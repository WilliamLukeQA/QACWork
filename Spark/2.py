from pyspark import SparkConf, SparkContext

def square(x):
	return x * x;  

con = SparkConf()
sc = SparkContext(conf = con)
list = [15,64,45,79.94]
rdd1 = sc.parallelize(list)
rdd2 = rdd1.map(square)
data = rdd2.collect()
print(data)
