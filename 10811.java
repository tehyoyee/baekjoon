// 10811.java
// 23.07.13. 04:23

import java.util.Scanner;

class Main {

	static int[] arr;

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);

		int N, M;
		N = sc.nextInt();
		M = sc.nextInt();

		arr = new int[N + 1];
		for (int i = 0; i < N + 1; i++) {
			arr[i] = i;
		}
		for (int o = 0; o < M; o++) {
			int i = sc.nextInt();
			int j = sc.nextInt();

			for (; i <= (i + j) / 2; i++, j--) {
				int tmp = arr[i];
				arr[i] = arr[j];
				arr[j] = tmp;
			}
		}
		for (int i = 1; i <= N; i++) {
			System.out.print(arr[i] + " ");
		}
	}
}