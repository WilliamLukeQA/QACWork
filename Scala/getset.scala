class Result{
	private var phy:Int = 0

	def physics_=(a:Int){
		if ((a >= 0) & (a <= 150)){
			phy = a
		}
		else{
			println("Value must be between 0 and 150")
		}
	}
	def physics:Int={
		return phy
	}
}

var Luke = new Result()
Luke.physics = 20
var Total = Luke.physics
print("Answer:"+Total)