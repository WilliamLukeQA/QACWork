class ONE{
	def message(){
		println("Hello")
	}
}

class TWO extends ONE{
	override def message(){
		print("Hey")
	}
}

var m = new TWO()
m.message

var k = new ONE()
k.message

