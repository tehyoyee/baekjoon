// 11723.java
// 23.08.12. 15:38 ~ 15:58

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		HashMap<Integer, Boolean> hashMap = new HashMap<>();
		for (int i = 1; i <= 20; i++) {
			hashMap.put(i, false);
		}
		int M = Integer.parseInt(br.readLine());
		
		for (; M > 0; M--) {

			int value = 0;
			st = new StringTokenizer(br.readLine());
			String order = st.nextToken();
			if (st.hasMoreTokens()) {
				value = Integer.parseInt(st.nextToken());
			}

			if (order.equals("add")) {
				hashMap.put(value, true);
			} else if (order.equals("remove")) {
				hashMap.put(value, false);
			} else if (order.equals("check")) {
				if (hashMap.get(value) == true) {
					sb.append("1\n");
				} else {
					sb.append("0\n");
				}
			} else if (order.equals("toggle")) {
				hashMap.put(value, !hashMap.get(value));
			} else if (order.equals("all")) {
				for (int i = 1; i <= 20; i++) {
					hashMap.put(i, true);
				}
			} else {
				for (int i = 1; i <= 20; i++) {
					hashMap.put(i, false);
				}
			}
		}
		System.out.print(sb);
	}
}