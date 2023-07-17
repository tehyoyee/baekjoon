// 1764.java
// 23.07.17. 22:35 ~

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		HashSet<String> set = new HashSet<>();
		ArrayList<String> result = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			set.add(br.readLine());
		}
		for (int i = 0; i < M; i++) {
			String str = br.readLine();
			if (set.contains(str)) {
				result.add(str);
			}
		}
		System.out.println(result.size());
		Collections.sort(result);
		for (String str : result) {
			System.out.println(str);
		}
	}
}