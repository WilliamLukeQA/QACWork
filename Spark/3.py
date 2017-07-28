from pyspark import SparkConf, SparkContext

def greater(x):
	if x > 50:
		return("Greater than 50")
	else:
		return("Less than 50")  

def normal(x):
	if x == "Luke":
		return("Ginger")
	else:
		return("Normal") 

con = SparkConf()
sc = SparkContext(conf = con)
#list = [15,64,45,79,94]
list = ["Harvey", "Richmond", "Luke", "J4m3s"]
rdd1 = sc.parallelize(list)
rdd2 = rdd1.map(normal)
data = rdd2.collect()
print(data)
