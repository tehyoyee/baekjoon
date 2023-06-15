// 10845.java
// 23.06.15.

import java.io.*;
import java.util.*;

class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		Deque<Integer> q = new LinkedList<>();

		int N = Integer.parseInt(st.nextToken());

		while (N-- > 0) {
			st = new StringTokenizer(br.readLine());
			String action = st.nextToken();
			if (action.equals("push")) {
				q.addLast(Integer.parseInt(st.nextToken()));
			} else if (action.equals("empty")) {
				if (q.isEmpty()) {
					System.out.println(1);
				} else {
					System.out.println(0);
				}
			} else if (action.equals("size")) {
				System.out.println(q.size());
			} else {
				if (q.isEmpty()) {
					System.out.println(-1);
				} else if (action.equals("pop")) {
					System.out.println(q.poll());
				} else if (action.equals("front")) {
					System.out.println(q.getFirst());
				} else {
					System.out.println(q.getLast());
				}
			}

		}
		
	}
}