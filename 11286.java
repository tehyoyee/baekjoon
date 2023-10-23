// 11286.java
// 23.10.23. 11:33 ~ 12:13	peek() 간의 비교는 주솟값의 비교이기에 안된다. intValue() 를  chaining 해서 써야한다.

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		PriorityQueue<Integer> minus = new PriorityQueue<>();
		PriorityQueue<Integer> plus = new PriorityQueue<>();
		StringBuilder sb = new StringBuilder();

		for (int i = 0; i < N; i++) {
			int input = Integer.parseInt(br.readLine());

			if (input == 0) {
				if (minus.isEmpty() && plus.isEmpty()) {
					sb.append('0').append('\n');
				} else if (plus.isEmpty()) {
					sb.append(-1 * minus.poll()).append('\n');
				} else if (minus.isEmpty()) {
					sb.append(plus.poll()).append('\n');
				} else if (minus.peek().intValue() == plus.peek().intValue()) {
					sb.append(-1 * minus.poll()).append('\n');
				} else if (minus.peek() < plus.peek()) {
					sb.append(-1 * minus.poll()).append('\n');
				} else {
					sb.append(plus.poll()).append('\n');
				}
			} else if (input < 0) {
				minus.add(-1 * input);
			} else {
				plus.add(input);
			}
		}
		System.out.print(sb);
	}
}