// 4134.java
// 23.08.07. 11:55

import java.util.*;
import java.io.*;
import java.math.BigInteger;

class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		int N = Integer.parseInt(br.readLine());
		Long[] lst = new Long[N];

		for (int i = 0; i < N; i++) {
			BigInteger x = new BigInteger(String.valueOf(Long.parseLong(br.readLine())));
			if (x.isProbablePrime(10)) {
				sb.append(x).append("\n");
			} else {
				sb.append(x.nextProbablePrime()).append("\n");
			}
		}	
		System.out.print(sb);
	}
}