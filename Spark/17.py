from pyspark import SparkConf, SparkContext

con = SparkConf()
sc = SparkContext(conf = con)

rdd1 = sc.textFile("file:///home/cloudera/Desktop/Spark/Movies/Movies.item")
rdd2 = sc.textFile("file:///home/cloudera/Desktop/Spark/Movies/Moving-Ratings-Done.data")

movie = rdd1.map(lambda x: x.encode("ascii", "ignore").split("|"))
movierat = rdd2.map(lambda x: x.encode("ascii", "ignore").split("\t"))

moviename = movie.map(lambda x: (x[0],x[1])).collect()
unknowngenre = movie.map(lambda x: (x[0],x[5])).collect()  

for a in moviename:
	if "GoldenEye" in a[1]:
		movieid = a[0]
		moviena = a[1]

def rate(z):
	if (z[1]==movieid)&(z[2]=='5'):
		return True
	else:
		return False

def genre(x):
	genrenum[0]=genrenum[0]+int(x[5])
	genrenum[1]=genrenum[1]+int(x[6])
	genrenum[2]=genrenum[2]+int(x[7])
	genrenum[3]=genrenum[3]+int(x[8])
	genrenum[4]=genrenum[4]+int(x[9])
	genrenum[5]=genrenum[5]+int(x[10])
	genrenum[6]=genrenum[6]+int(x[11])
	genrenum[7]=genrenum[7]+int(x[12])
	genrenum[8]=genrenum[8]+int(x[13])
	genrenum[9]=genrenum[9]+int(x[14])
	genrenum[10]=genrenum[10]+int(x[15])
	genrenum[11]=genrenum[11]+int(x[16])
	genrenum[12]=genrenum[12]+int(x[17])
	genrenum[13]=genrenum[13]+int(x[18])
	genrenum[14]=genrenum[14]+int(x[19])
	genrenum[15]=genrenum[15]+int(x[20])
	genrenum[16]=genrenum[16]+int(x[21])
	genrenum[17]=genrenum[17]+int(x[22])
	genrenum[18]=genrenum[18]+int(x[23])

	return genrenum

	
genrenum =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
send = movie.map(genre)
genrenum = send.collect()

ratingid = movierat.filter(rate)
num = str(ratingid.count())

print "unknown %s action %s adventure %s animation %s childrens %s comedy %s crime %s documentary %s drama %s fantasy %s film-noir %s horror %s musical %s mystery %s romance %s sci-fi %s thriller %s war %s western %s"%(genrenum[1681][0],genrenum[1681][1],genrenum[1681][2],genrenum[1681][3],genrenum[1681][4],genrenum[1681][5],genrenum[1681][6],genrenum[1681][7],genrenum[1681][8],genrenum[1681][9],genrenum[1681][10],genrenum[1681][11],genrenum[1681][12],genrenum[1681][13],genrenum[1681][14],genrenum[1681][15],genrenum[1681][16],genrenum[1681][17],genrenum[1681][18])
print "%s, has %s ratings that are 5 stars"%(moviena,num)
