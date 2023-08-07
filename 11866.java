// 11866.java
// 23.08.07. 11:24 ~ 11:49

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());
		LinkedList<Integer> list = new LinkedList<>();
		
		int N, K;
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		for (int i = 1; i <= N; i++) {
			list.add(i);
		}

		sb.append("<");
		while (!list.isEmpty()) {
			for (int i = 1; i < K; i++) {
				list.add(list.getFirst());
				list.removeFirst();
			}
			sb.append(list.getFirst()).append(", ");
			list.removeFirst();
		}
		sb.deleteCharAt(sb.lastIndexOf(" "));
		sb.deleteCharAt(sb.lastIndexOf(","));
		sb.append(">");
		System.out.println(sb);
	}
}