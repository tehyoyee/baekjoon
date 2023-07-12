// 2444.java
// 23.07.13. 04:05

import java.util.Scanner;

class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();

		int i = N - 1;
		int j = 1;
		while (i > 0) {
			for (int k = 0; k < i; k++)
				System.out.print(" ");
			for (int k = 0; k < j; k++)
				System.out.print("*");
			System.out.println();
			i--;
			j += 2;
		}
		
		while (i < N) {
			for (int k = 0; k < i; k++)
				System.out.print(" ");
			for (int k = 0; k < j; k++)
				System.out.print("*");
			System.out.println();
			i++;
			j -= 2;
		}
		sc.close();
	}
}