// 10810.java
// 23.07.13. 03:34

import java.util.Scanner;

class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();

		int[] arr = new int[N];
		for (int i = 0; i < M; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			int c = sc.nextInt();
			for (int j = a - 1; j < b; j++) {
				arr[j] = c;
			}
		}
		for (int i = 0; i < N; i++) {
			System.out.print(arr[i] + " ");
		}
		sc.close();
	}
}