// 11279.java
// 23.12.18. 17:24 ~ 17:30

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		PriorityQueue<Integer> q = new PriorityQueue<>();

		int N = Integer.parseInt(br.readLine());
		for (int i = 0; i < N; i++) {
			int input = Integer.parseInt(br.readLine());

			if (input == 0) {
				if (q.isEmpty()) {
					sb.append("0\n");
				} else {
					sb.append(-q.poll()).append("\n");
				}
			} else {
				q.add(-input);
			}
		}
		System.out.print(sb);
	}
}