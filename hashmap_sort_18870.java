// 18870.java
// 23.07.18. 12:04 ~ x

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		HashMap<Integer, Integer> hashMap = new HashMap<>();

		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N];
		int[] sortedArr = new int[N];
		st = new StringTokenizer(br.readLine());
		int rank = 0;
		for (int i = 0; i < N; i++) {
			int input = Integer.parseInt(st.nextToken());
			arr[i] = sortedArr[i] = input;
		}
		Arrays.sort(sortedArr);
		for (int i = 0; i < N; i++) {
			if (!hashMap.containsKey(sortedArr[i])) {
				hashMap.put(sortedArr[i], rank);
				rank++;
			}
		}
		for (int x : arr) {
			sb.append(hashMap.get(x)).append(" ");
		}
		System.out.println(sb);
	}
}