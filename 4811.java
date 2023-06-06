// 4811.java
// 23.06.07. 07:58 ~

import java.io.*;

class Main {

	static Long[] dp;
	static int input;
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		dp = new Long[31];

		dp[0] = 1L;
		dp[1] = 1L;
		dp[2] = 2L;
		for (int i = 3; i < 31; i++) {
			dp[i] = 0L;
			for (int j = 0; j < i; j++) {
				dp[i] += dp[j] * dp[i-1-j];
			}
		}

		while (true) {
			input = Integer.parseInt(br.readLine());
			if (input == 0)
				return;
			System.out.println(dp[input]);
		}
	}
}
