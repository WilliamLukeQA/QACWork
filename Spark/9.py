from pyspark import SparkConf, SparkContext
  
def add(a,b):
	return a+b

con = SparkConf()
sc = SparkContext(conf = con)

list =[1,2,3,4,5,6,7,8,9,10]
rdd1 = sc.parallelize(list)
addition = rdd1.reduce(add)

print addition

