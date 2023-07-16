// 1654.java
// 23.07.17. 05:30 ~

import java.util.*;
import java.io.*;

class Main {
	static int N, M;
	static long[] lans;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		M = Integer.parseInt(st.nextToken());
		N = Integer.parseInt(st.nextToken());
		lans = new long[M];
		long lanMax = 0;
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			lans[i] = Integer.parseInt(st.nextToken());
			lanMax = Math.max(lanMax, lans[i]);
		}

		long start = 0;
		long end = lanMax + 1;
		long mid = (start + end) / 2;

		while (start < end) {
			mid = (end + start) / 2;

			if (N > getPart(mid)) {
				end = mid;
			} else {
				start = mid + 1;
			}
		}
		System.out.println(start - 1);
	}

	static public int getPart(long mid) {
		int result = 0;

		for (int i = 0; i < M; i++) {
			result += lans[i] / mid;
		}
		return result;
	}
}
