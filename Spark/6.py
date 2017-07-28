from pyspark import SparkConf, SparkContext
  
con = SparkConf()
sc = SparkContext(conf = con)
list = [15,64,45,79,94]
rdd1 = sc.parallelize(list)
rdd2 = rdd1.filter(lambda x: True if x > 50 else False)
data = rdd2.collect()
print(data)
