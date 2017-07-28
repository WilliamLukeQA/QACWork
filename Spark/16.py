from pyspark import SparkConf, SparkContext

con = SparkConf()
sc = SparkContext(conf = con)

rdd1 = sc.textFile("file:///home/cloudera/Desktop/Spark/Movies/Movies.item")
rdd2 = sc.textFile("file:///home/cloudera/Desktop/Spark/Movies/Moving-Ratings-Done.data")

def findmovie(x):
	moviename = x.split("|")
	return moviename[1][1]

datamovie = rdd1.map(findmovie)
datamovies = datamovie.collect()

print datamovies
 
