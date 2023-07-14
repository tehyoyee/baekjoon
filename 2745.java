// 2745.java
// 23.07.15. 02:19

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int result = 0;
		String str = st.nextToken();
		int pt = Integer.parseInt(st.nextToken());

		for (int i = 0; i < str.length(); i++) {
			result *= pt;
			if (Character.isDigit(str.charAt(i))) {
				result += (int)(str.charAt(i) - '0');
			} else {
				result += (int)(str.charAt(i) - 'A') + 10;
			}
		}
		System.out.println(result);
	}
}