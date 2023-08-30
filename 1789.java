// 1789.java
// 23.08.30. 15:15 ~ 15:33

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		long N = Long.parseLong(br.readLine());
		long sum = 0;
		long i = 2;
		while (true) {
			sum += i;
			if (sum >= N) { break; }
			i++;
		}
		System.out.println(--i);
	}
}

