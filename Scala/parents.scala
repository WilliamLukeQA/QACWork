class ONE{
	def drawing(){
		println("Draw Something")
	}
}

class TWO extends ONE{
	override def drawing(){
		println("Draw Line")
	}
}

var x:ONE = new TWO()
x.drawing()
