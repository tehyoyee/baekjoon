// 25304.java
// 23.07.13. 03:29

import java.util.Scanner;

class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int X = sc.nextInt();
		int N = sc.nextInt();
		int result = 0;

		for (int i = 0; i < N; i++) {
			result += sc.nextInt() * sc.nextInt();
		}
		if (X == result) {
			System.out.println("Yes");
		} else {
			System.out.println("No");
		}
	}
}