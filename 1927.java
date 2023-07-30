// 1927.java
// 23.07.30 23:30 ~ 23:38

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		PriorityQueue<Integer> queue = new PriorityQueue<>();

		int N = Integer.parseInt(br.readLine());
		for (int i = 0; i < N; i++) {
			int input = Integer.parseInt(br.readLine());

			if (input == 0) {
				if (queue.isEmpty()) {
					sb.append(0).append('\n');
				} else {
					sb.append(queue.poll()).append('\n');
				}
			} else {
				queue.add(input);
			}
		}
		System.out.println(sb);
	}
}