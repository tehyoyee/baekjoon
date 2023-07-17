// 10866.java
// 23.07.17. 22:16 ~ 22:32

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int N = Integer.parseInt(br.readLine());
		Deque<Integer> deque = new LinkedList<>();

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			String cmd = st.nextToken();
			int value = 0;
			if (st.hasMoreTokens()) {
				value = Integer.parseInt(st.nextToken());
			}
			if (cmd.equals("push_back")) {
				deque.addLast(value);
			} else if (cmd.equals("push_front")) {
				deque.addFirst(value);
			} else if (cmd.equals("pop_front")) {
				if (!deque.isEmpty()) {
					System.out.println(deque.getFirst());
					deque.removeFirst();
				} else {
					System.out.println(-1);
				}
			} else if (cmd.equals("pop_back")) {
				if (!deque.isEmpty()) {
					System.out.println(deque.getLast());
					deque.removeLast();
				} else {
					System.out.println(-1);
				}
			} else if (cmd.equals("size")) {
				System.out.println(deque.size());
			} else if (cmd.equals("empty")) {
				if (deque.isEmpty()) {
					System.out.println(1);
				} else {
					System.out.println(0);
				}
			} else if (cmd.equals("front")) {
				if (!deque.isEmpty()) {
					System.out.println(deque.peekFirst());
				} else {
					System.out.println(-1);
				}
			} else {
				if (!deque.isEmpty()) {
					System.out.println(deque.peekLast());
				} else {
					System.out.println(-1);
				}
			}
		}			
	}
}