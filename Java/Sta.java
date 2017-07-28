
public class Sta {
	static int Dollar;
	
	static{
		Dollar = 10+1+15;
	}
	public void SetDollar(int a){
		Dollar = a;
	}
	public void ConvertMoney(int a){
		System.out.println(Dollar * a);
	}
}
