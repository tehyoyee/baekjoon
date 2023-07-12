// 10813.java
// 23.07.13. 03:51

import java.util.Scanner;

class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int[] arr = new int[N+1];
		for (int i = 0; i < N+1; i++) {
			arr[i] = i;
		}
		for (int i = 0; i < M; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			int tmp = arr[a];
			arr[a] = arr[b];
			arr[b] = tmp;
		}
		for (int i = 1; i < N + 1; i++) {
			System.out.print(arr[i] + " ");
		}
	}
}