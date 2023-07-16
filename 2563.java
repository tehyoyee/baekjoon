// 2563.java
// 23.07.17. 05:15 ~

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		boolean[][] arr = new boolean[100][100];
		int result = 0;
		int N = Integer.parseInt(st.nextToken());
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			for (int j = a; j < a + 10; j++) {
				for (int k = b; k < b + 10; k++) {
					arr[j][k] = true;
				}
			}
		}
		for (int i = 0; i < 100; i++) {
			for (int j = 0; j < 100; j++) {
				if (arr[i][j] == true) {
					result++;
				}
			}
		}
		System.out.println(result);
	}
}