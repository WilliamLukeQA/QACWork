from pyspark import SparkConf, SparkContext

conf = SparkConf()
sc = SparkContext(conf = conf)
rddmovies = sc.textFile("file:///home/cloudera/Desktop/Spark/Movies/Movies.item")
rddratings = sc.textFile("file:///home/cloudera/Desktop/Spark/Movies/Moving-Ratings-Done.data")
datamovies = rddmovies.map(lambda x: x.encode("ascii", "ignore").split("|")).collect()
dataratings = rddratings.map(lambda x: x.encode("ascii", "ignore").split("\t")).collect()

ratingcount5most = 0
ratingcount5mostmovie = ""

for moviesloop in datamovies:
	ratingcount5 = 0 
	for ratingsloop in dataratings: 		
		if moviesloop[0] == ratingsloop[1]: 	
			if ratingsloop[2] == "5":
				ratingcount5 = ratingcount5 + 1					
	if ratingcount5 > ratingcount5most:
		ratingcount5most = ratingcount5
		ratingcount5mostmovie = moviesloop[1]

print ratingcount5mostmovie, ratingcount5most
