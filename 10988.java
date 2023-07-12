// 10988.java
// 23.07.13. 04:50

import java.util.Scanner;

class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int result = 1;
		String str = sc.nextLine();
		for (int i = 0; i < str.length() / 2; i++) {
			if (str.charAt(i) != str.charAt(str.length() - i - 1)) {
				result = 0;
				break;
			}
		}
		System.out.println(result);
		sc.close();
	}
}