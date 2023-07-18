// 18258.java
// 23.07.18. 11:33 ~

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		Deque<Integer> deque = new LinkedList<>();
		StringBuilder sb = new StringBuilder();

		int N = Integer.parseInt(br.readLine());

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int value = 0;
			String cmd = st.nextToken();
			if (st.hasMoreTokens()) {
				value = Integer.parseInt(st.nextToken());
			}
			if (cmd.equals("push")) {
				deque.add(value);
			} else if (cmd.equals("pop")) {
				if (!deque.isEmpty()) {
					sb.append(deque.getFirst()).append('\n');
					deque.removeFirst();
				} else {
					sb.append(-1).append('\n');
				}
			} else if (cmd.equals("size")) {
				sb.append(deque.size()).append('\n');
			} else if (cmd.equals("empty")) {
				if (deque.isEmpty()) {
					sb.append(1).append('\n');
				} else {
					sb.append(0).append('\n');
				}
			} 
			else if (cmd.equals("front")) {
				if (!deque.isEmpty()) {
					sb.append(deque.getFirst()).append('\n');
				} else {
					sb.append(-1).append('\n');
				}
			} else {
				if (!deque.isEmpty()) {
					sb.append(deque.getLast()).append('\n');
				} else {
					sb.append(-1).append('\n');
				}
			}
		}
		System.out.println(sb);
	}
}