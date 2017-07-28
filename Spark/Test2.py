from pyspark import SparkConf,SparkContext

con=SparkConf()
sc=SparkContext(conf=con)

In1=sc.textFile("file:///home/cloudera/Desktop/Spark/result.csv")
header=In1.take(1)[0]
In1NoHead=In1.filter(lambda x:x != header)
Results=In1NoHead.map(lambda x: x.encode("ascii", "ignore").split(","))

In2=sc.textFile("file:///home/cloudera/Desktop/Spark/personal.csv")
header=In2.take(1)[0]
In2NoHead=In2.filter(lambda x:x != header)
Info=In2NoHead.map(lambda x: x.encode("ascii", "ignore").split(","))

CInfo=Info.collect()
SResults=Results.map(lambda x: (x[0],x[2]))
CResults=SResults.collect()
InfoLength=Info.count()

def Add(s):
	a=0
	Temp=[]
	ResultsLength=Results.count()
	A=1
	while a<InfoLength:
		Z=0
		Y=0
		while s[A][0]==CInfo[a][0]:
			Z=Z+int(s[A][1])
			A=A+1
			Y=Y+1
			if A>=ResultsLength:
				break
		a=a+1
		Temp=Temp+[[str(a),Z,Y]]

	return Temp
Total=Add(CResults)



def Per(a):
	Temp2=[]
	A=0
	while A<InfoLength:
		B=A+1
		C=(a[A][1]*100)/450
		A=A+1
		Temp2=Temp2+[[str(B),C]]
	return Temp2

Percentage=Per(Total)




def Grad(a):
	if a>=90:
		print "Grade: A*"
	elif 80<=a<90:
		print "Grade: A"
	elif 70<=a<80:
		print "Grade: A"
	elif 60<=a<70:
		print "Grade: A"
	elif a<60:
		print "Grade: Fail"
U=0
A=0
for F in CInfo:
	print "RegNo: %s" %F[0]
	print "Name: %s" %F[1]
	print "Address: %s" %F[2]
	for B in Total:
		if B[0]==F[0]:
			print "Total Marks: %s" %B[1]
	for C in Percentage:
		if C[0]==F[0]:
			print "Percentage: %s"  %C[1]
			Grad(C[1])
	if Total[U][2]!=3:
		print "Didn't Have All Three Marks"

	print ""
	
	if Percentage[U][1]>A:
		A=Percentage[U][1]
		High=F
	U=U+1
print "Student With Highest Mark:"
print ""
print "RegNo: %s" %High[0]
print "Name: %s" %High[1]
print "Address: %s" %High[2]
for B in Total:
	if B[0]==High[0]:
		print "Total Marks: %s" %B[1]
for C in Percentage:
	if C[0]==High[0]:
		print "Percentage: %s"  %C[1]
		Grad(C[1])
