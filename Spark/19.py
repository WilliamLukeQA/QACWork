from pyspark import SparkConf, SparkContext

con = SparkConf()
sc = SparkContext(conf = con)

rdd1 = sc.textFile("file:///home/cloudera/Desktop/Spark/Movies/Movies.item")
rdd2 = sc.textFile("file:///home/cloudera/Desktop/Spark/Movies/Moving-Ratings-Done.data")
rdd3 = sc.textFile("file:///home/cloudera/Desktop/Spark/Movies/Users.txt")

movie = rdd1.map(lambda x: x.encode("ascii", "ignore").split("|"))
movierat = rdd2.map(lambda x: x.encode("ascii", "ignore").split("\t"))
users = rdd3.map(lambda x: x.encode("ascii", "ignore").split("|"))

def under18(x):
	if int(x[1]) <= 18:
		return True
	else:
		return False

def countrate(x):
	if x[0] in a:
		return True
	else:
		return False
	
ages = users.map(lambda x: (x[0],x[1]))
eighteen = ages.filter(under18)
a=eighteen.collect()
ratings = movierat.filter(countrate)

print ratings.collect()
