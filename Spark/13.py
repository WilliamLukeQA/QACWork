from pyspark import SparkConf, SparkContext

con = SparkConf()
sc = SparkContext(conf = con)

rdd1 = sc.textFile("file:///home/cloudera/Desktop/Spark/trainee.txt")
rdd2 = sc.textFile("file:///home/cloudera/Desktop/Spark/trainer.txt")

convert1 = rdd1.map(lambda x: x.encode("ascii","ignore"))
convert2 = rdd2.map(lambda x: x.encode("ascii","ignore"))

#Union
resultrdd = convert1.union(convert2)
resultrdd2 = resultrdd.collect()
#Intesect
resultrddinter = convert1.intersection(convert2)
resultrdd2inter= resultrddinter.collect()
#Subtract
resultrddsub = convert1.subtract(convert2)
resultrdd2sub = resultrddsub.collect()

print "Union",resultrdd2
print "Intersection",resultrdd2inter 
print "Subtract",resultrdd2sub 
