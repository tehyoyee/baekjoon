// 10798.java
// 23.07.15. 01:43

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();

		String[] arr = new String[5];
		for (int i = 0; i < 5; i++) {
			st = new StringTokenizer(br.readLine());
			arr[i] = st.nextToken();
		}

		for (int j = 0; j < 15; j++) {
			for (int i = 0; i < 5; i++) {
				if (arr[i].length() <= j)
					continue;
				sb.append(arr[i].charAt(j));
			}
		}
		System.out.println(sb);
	}
}
