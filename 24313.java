// 24313.java
// 23.08.07. 13:36 ~

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int a, b;

		a = Integer.parseInt(st.nextToken());
		b = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(br.readLine());
		int n0 = Integer.parseInt(br.readLine());
		
		if (a == c) {
			if (b <= 0) {
				System.out.println(1);
			} else{
				System.out.println(0);
			}
		} else if (a * n0 + b <= c * n0 && a < c) {
			System.out.println(1);
		} else {
			System.out.println(0);
		}
	}
}