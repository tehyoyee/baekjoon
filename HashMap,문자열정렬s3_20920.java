// 20920.java
// 23.08.30. 15:38 ~

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		HashMap<String, Integer> map = new HashMap<>();

		for (int i = 0; i < N; i++) {
			String input = br.readLine();
			if (input.length() < M) {
				continue ;
			}
			if (map.containsKey(input)) {
				map.put(input, map.get(input) + 1);
			} else {
				map.put(input, 1);
			}
		}
		List<String> list = new ArrayList<>(map.keySet());
		Collections.sort(list, new Comparator<String>() {
			@Override
			public int compare(String o1, String o2) {
				if (Integer.compare(map.get(o1), map.get(o2)) != 0) {
					return Integer.compare(map.get(o2), map.get(o1));
				}
				if (o1.length() != o2.length()) {
					return o2.length() - o1.length();
				}
				return o1.compareTo(o2);
			}
		});
		StringBuilder sb = new StringBuilder();
		for (String x : list) {
			sb.append(x + "\n");
		}
		System.out.print(sb);
	}
}
