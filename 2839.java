// 2839.java
// 23.12.18. 15:19 ~ 15:27

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		int big = 0;
		int small = 0;

		big = N / 5;
		N %= 5;
		while (big >= 0 && N % 3 != 0) {
			N += 5;
			big--;
		}
		if (big < 0) {
			System.out.println(-1);
		} else {
			small = N / 3;
			System.out.println(big+small);
		}
	}
}