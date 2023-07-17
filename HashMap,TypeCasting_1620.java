// 1620.java
// 23.07.17 22:55 ~

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N, M;
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		HashMap<String, Integer> map = new HashMap<>();
		String[] names = new String[N + 1];

		for (int i = 1; i < N + 1; i++) {
			String input = br.readLine();
			map.put(input, i);
			names[i] = input;
		}
		for (int i = 0; i < M; i++) {
			String str = br.readLine();
			
			if (isDigit(str)) {
				int idx = Integer.parseInt(str);
				System.out.println(names[idx]);
			} else {
				System.out.println(map.get(str));
			}
		}
	}

	static boolean isDigit(String str) {
		try {
			Double double1 = Double.parseDouble(str);
			return true;
		} catch (NumberFormatException e) {
			return false;
		}
	}
}