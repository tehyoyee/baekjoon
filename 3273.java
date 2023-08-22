// 3273.java
// 23.08.22. 16:07 ~

import java.io.*;
import java.util.*;

class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int result = 0;
		int n = Integer.parseInt(br.readLine());
		int[] lst = new int[n];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			lst[i] = Integer.parseInt(st.nextToken());
		}
		int target = Integer.parseInt(br.readLine());
		int s = 0;
		int e = n - 1;
		Arrays.sort(lst);
		while (s < e) {
			int x = lst[s] + lst[e];
			if (target == x) {
				s++;
				e--;
				result++;
			} else if (target > x) {
				s++;
			} else {
				e--;
			}
		}
		System.out.println(result);
	}
}