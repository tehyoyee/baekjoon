// 2309.java
// 23.07.15. 02:02

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int x = 0, y = 0;
		int sum = 0;
		int[] h = new int[9];
		for (int i = 0; i < 9; i++) {
			st = new StringTokenizer(br.readLine());
			h[i] = Integer.parseInt(st.nextToken());
			sum += h[i];
		}

		Arrays.sort(h);
		for (int i = 0; i < 8; i++) {
			for (int j = i + 1; j < 9; j++) {
				if (sum - h[i] - h[j] == 100) {
					x = i;
					y = j;
					break;
				}
			}
			if (x != 0 || y != 0) {
				break;
			}
		}
		for (int i = 0; i < 9; i++) {
			if (i != x && i != y) {
				System.out.println(h[i]);
			}
		}
	}
}