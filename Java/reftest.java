
public class reftest {

	public static void main(String args[]) {
	
		ref x;
		
		x = new ref();
		
		
		System.out.println(x.a);
		
		x.a = 400;
		
		System.out.println(x.a);
		x.message();
	}
}
