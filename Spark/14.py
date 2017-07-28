from pyspark import SparkConf, SparkContext

con = SparkConf()
sc = SparkContext(conf = con)

list1 = [1,2,3,4,5,6,7,8,9]
rdd1 = sc.parallelize(list1,3)
rdd1.saveAsTextFile("file:///home/cloudera/Desktop/Spark/parts.txt")

