// 2501.java
// 23.07.15. 02:46

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int result = 0;
		int cnt = 1;

		for (int i = 1; i <= N; i++) {
			if (N % i == 0) {
				if (cnt == K) {
					result = i;
					break;
				} else {
					cnt++;
				}
			}
		}
		System.out.println(result);
	}
}