// 1966.java
// 23.08.13. 22:51 ~

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		int testCnt = Integer.parseInt(br.readLine());

		for (; testCnt > 0; testCnt--) {
			LinkedList<X> lst = new LinkedList<>();
			PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			st = new StringTokenizer(br.readLine());
			int cnt = 1;

			for (int i = 0; i < N; i++) {
				int tmp = Integer.parseInt(st.nextToken());
				priorityQueue.add(tmp);
				lst.add(new X(tmp, i));
			}
			while (true) {
				X x = lst.poll();
				if (priorityQueue.peek() <= x.value) {
					if (x.order == M) {
						sb.append(cnt).append("\n");
						break;
					}
					cnt++;
					priorityQueue.poll();
				} else {
					lst.add(x);
				}
			}
		}
		System.out.print(sb);
	}

	static class X {
		int value;
		int order;

		X(int v, int o) {
			value = v;
			order = o;
		};
	}

}