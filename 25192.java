// 25192.java
// 23.10.23. 11:23 ~

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Map<String, Integer> map = new HashMap<>();;

		int result = 0;
		int N = Integer.parseInt(br.readLine());
		for (int i = 0; i < N; i++) {
			String input = br.readLine();
			if (input.equals("ENTER")) {
				map = new HashMap<>();
			}
			else if (map.containsKey(input)) {
				continue;
			} else {
				map.put(input,1);
				result++;
			}
		}
		System.out.println(result);
	}
}