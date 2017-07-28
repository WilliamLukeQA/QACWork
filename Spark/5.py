from pyspark import SparkConf, SparkContext

def check(x):
	if x > 50:
		return True
	else:
		return False   

con = SparkConf()
sc = SparkContext(conf = con)
list = [15,64,45,79,94]
rdd1 = sc.parallelize(list)
rdd2 = rdd1.filter(check)
data = rdd2.collect()
print(data)
