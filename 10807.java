// 10807.java
// 23.07.13. 02:32

import java.util.Scanner;

class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int []arr = new int[N];
		int result = 0;

		for (int i = 0; i < N; i++) {
			arr[i] = sc.nextInt();
		}
		int v = sc.nextInt();
		for (int x : arr) {
			if (x == v) {
				++result;
			}
		}
		System.out.println(result);
		sc.close();
	}
}