// 15

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int N = Integer.parseInt(br.readLine());
		int[] A = new int[N];
		Integer[] B = new Integer[N];
		int result = 0;
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			A[i] = Integer.parseInt(st.nextToken());
		}
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			B[i] = Integer.parseInt(st.nextToken());
		}

		Arrays.sort(A);
		Arrays.sort(B, new Comparator<Integer>() {
			@Override
			public int compare(Integer o1, Integer o2) {
				return o2 - o1;
			}
		});
		for (int i = 0; i < N; i++) {
			result += A[i] * B[i];
		}
		System.out.println(result);
	}
}