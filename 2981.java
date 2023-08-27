// 2981.java
// 23.08.28. 00:26 ~

import java.util.*;
import java.io.*;

class Main {

	static int N;
	static int[] arr;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		N = Integer.parseInt(br.readLine());
		arr = new int[N];
	
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		Arrays.sort(arr);
		int gcdV = arr[1] - arr[0];
		for (int i = 2; i < N; i++) {
			gcdV = gcd(gcdV, arr[i] - arr[i - 1]);
		}
		for (int i = 2; i <= gcdV; i++) {
			if (gcdV % i == 0) {
				sb.append(i + " ");
			}
		}
		sb.deleteCharAt(sb.length() - 1);
		System.out.println(sb);

	}
	
	static int gcd(int a, int b) {
		while (b != 0) {
			int r = a % b;
			a = b;
			b = r;
		}
		return a;
	}
}