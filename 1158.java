// 1158.java
// 23.07.17. 23:17 ~

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		LinkedList<Integer> lst = new LinkedList<>();
		int N, M;
		
		sb.append("<");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		for (int i = 0; i < N; i++) {
			lst.add(i);
		}

		int idx = 0;
		while (!lst.isEmpty()) {
			idx = (idx + M - 1) % lst.size();
			sb.append(lst.get(idx) + 1).append(", ");
			lst.remove(idx);
		}
		sb.deleteCharAt(sb.length()-1);
		sb.deleteCharAt(sb.length()-1);
		sb.append(">");
		System.out.println(sb);
	}
}