def convert(a:Int):String = {
	var b:Int = (a / 1000)
	var c:String = ""
	if(b >=1){
			b match {
			case 1 => c = c + "One Thousand"
			case 2 => c = c + "Two Thousand"
			case 3 => c = c + "Three Thousand"
			case 4 => c = c + "Four Thousand"
			case 5 => c = c + "Five Thousand"
			case 6 => c = c + "Six Thousand"
			case 7 => c = c + "Seven Thousand"
			case 8 => c = c + "Eight Thousand" 
			case 9 => c = c + "Nine Thousand"
			case 10 => c = c + "Ten Thousand"
		}
		println(c)
	} else {
		return "Error"
	}


println("Converted:"+convert(7000))