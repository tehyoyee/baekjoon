// 9086.java
// 23.07.14. 11:33

import java.util.*;

class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int T = Integer.parseInt(sc.nextLine());

		for (int i = 0; i < T; i++) {
			String input = sc.nextLine();
			System.out.println(input.charAt(0) + "" + input.charAt(input.length() - 1));
		}
		sc.close();
	}
}