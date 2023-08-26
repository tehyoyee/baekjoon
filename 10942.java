// 10942.java
// 23.08.26. 19:51 ~

import java.util.*;
import java.io.*;

class Main {

	static int N, M;
	static int[] arr;
	static int[][] dp;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();

		N = Integer.parseInt(br.readLine());
		arr = new int[N + 1];

		st = new StringTokenizer(br.readLine());
		for (int i = 1; i < N + 1; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		dp = new int[N + 1][N + 1];
		for (int i = 1; i < N + 1; i++) {
			for (int j = i; j < N + 1; j++) {
				if (check(i, j) == true) {
					dp[i][j] = 1;
				} else {
					dp[i][j] = 0;
				}
			}
		}

		M = Integer.parseInt(br.readLine());
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			sb.append(dp[Integer.parseInt(st.nextToken())][Integer.parseInt(st.nextToken())]).append('\n');
		}
		System.out.print(sb);
	}

	public static Boolean check(int s, int e) {
		for (int i = 0; i < (e - s) / 2; i++) {
			if (arr[s + i] != arr[e - i]) {
				return false;
			}
		}
		return true;
	}
}
