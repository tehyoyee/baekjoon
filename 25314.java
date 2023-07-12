// 25314.java
// 23.07.13. 03:23

import java.util.Scanner;

class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt() / 4;

		for (int i = 0; i < N; i++) {
			System.out.print("long ");
		}
		System.out.println("int");
		sc.close();
	}
}