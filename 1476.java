// 1476.java
// 23.10.18. 11:29 ~ 11:47

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int E = Integer.parseInt(st.nextToken());
		int S = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int result = 1;

		while (true) {
			if (E == S && S == M)
				break;
			int x = function(E, S, M);
			if (x == 0) {
				E += 15;
			} else if (x == 1) {
				S += 28;
			} else {
				M += 19;
			}
		}
		System.out.println(E);
	}

	public static int function(int E, int S, int M) {
		if (E <= S && E <= M)
			return 0;
		if (M < E && M <= S)
			return 2;
		return 1;
	}
}