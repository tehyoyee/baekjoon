// // 2565.java

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int[][] arr = new int[N][2];
		int[] dp = new int[N];
		int result = 0;
		for (int i = 0; i < N; i++){
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 2; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		dp[0] = 1;
		Arrays.sort(arr, new Comparator<int[]>() {
			@Override
			public int compare(int[] a, int[] b) {
				return a[0] - b[0];
			}
		});

		for (int i = 1; i < N; i++) {
			dp[i] = 1;
			for (int j = i - 1; j >= 0; j--) {
				if (arr[j][1] < arr[i][1]) {
					dp[i] = Math.max(dp[j] + 1, dp[i]);
				}
			}
			result = Math.max(dp[i], result);
		}
		System.out.println(N - result);
	}
}
