import org.apache.spark.{SparkConf, SparkContext}

val conf = new SparkConf()
val sc = new SparkContext(conf)

val datalist = List(1,2,3,4,5,6,7,8,9)
println(datalist)   
