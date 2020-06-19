package Fibonacci;

import java.math.BigDecimal;

public class Fibonacci {
	public static BigDecimal of(int n){
		
		BigDecimal a = BigDecimal.valueOf(1);
		BigDecimal b = BigDecimal.valueOf(1);
		
		for(int i=3; i<=n; i++) {
			BigDecimal temp = a.add(b);
			a = b;
			b = temp;
		}
		return b;
	}
	
	public static void main(String[] args) {
		
		for(int i=1;i<=200;i++) {
			System.out.println(Integer.toString(i) +':' +Fibonacci.of(i));
		}

	}
	
}


	

