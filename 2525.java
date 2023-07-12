// 2525.java
// 23.07.13. 02:13 ~

import java.util.Scanner;

class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();

		if (b + c%60 >= 60) {
			++a;
		}
		b = (b + c)%60;
		System.out.println((a + c/60)% 24 + " " + b);
		sc.close();
	}
}