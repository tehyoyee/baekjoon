// 27866.java
// 23.07.13. 03:17

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		String S = st.nextToken();
		st = new StringTokenizer(br.readLine());
		int i = Integer.parseInt(st.nextToken());
		System.out.println(S.charAt(i-1));
	}
}