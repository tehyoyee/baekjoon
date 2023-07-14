// 2738.java
// 23.07.15.

import java.util.*;

class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);

		int N, M;
		N = sc.nextInt();
		M = sc.nextInt();
		int[][] arr = new int[N][M];

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				arr[i][j] = sc.nextInt();
			}
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				arr[i][j] += sc.nextInt();
			}
		}
		for (int[] tmp : arr) {
			for (int x : tmp) {
				System.out.print(x +  " ");
			}
			System.out.println();
		}
	}
}