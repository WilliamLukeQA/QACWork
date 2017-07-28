var Physics : Int = 70
var Maths : Int = 46
var Chemistry : Int = 50

var Total : Int = Physics + Maths + Chemistry
var Per = Total * 100 / 300
var Pass : String = "Passed"

if (Per < 60){
	Pass = "Did Not Pass"
}

println(" ")
println("Total Marks:" +Total)
println("Percentage:" +Per+("%"))
println("Pass:" +Pass)


def add(a:Int,b:Int):Int={
	var c = a + b
	return c
}

println("Answer is:"+add(2,3))

def word(a:Int):String={
	a match {
		case 0 => "Zero"
		case 1 => "One"
		case 2 => "Two"
		case 3 => "Three"
		case 4 => "Four"
		case 5 => "Five"
		case 6 => "Six"
		case 7 => "Seven"
		case 8 => "Eight" 
		case 9 => "Nine"
		case 10 => "Ten"
	}
}

println("Convert:"+word(2))

