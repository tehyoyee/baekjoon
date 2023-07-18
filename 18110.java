// 18110.java
// 23.07.18. 11:02 ~ 11:31

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N];
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}

		Arrays.sort(arr);
		int total = 0;

		int percent15 = (int)Math.round(N * 0.15);
		for (int i = percent15; i < N - percent15; i++) {
			total += arr[i];
		}
		System.out.println((int)Math.round(((double)total / (double)(N - percent15 * 2))));
	}
}