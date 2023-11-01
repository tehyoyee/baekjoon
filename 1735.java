// 1735.java
// 23.11.01. 09:31 ~

import java.util.*;
import java.io.*;

class Main {

	static int[] fraction;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		st = new StringTokenizer(br.readLine());
		int a = Integer.parseInt(st.nextToken());
		int b = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		int c = Integer.parseInt(st.nextToken());
		int d = Integer.parseInt(st.nextToken());

		int numerator = a * d + b * c;
		int denominator = b * d;
		int mod = gcd(numerator, denominator);
		System.out.println(numerator / mod + " " + denominator / mod);
	}

	public static int gcd(int a, int b) {
		if (a < b) {
			int tmp;
			tmp = a;
			a = b;
			b = tmp;
		}

		if (b == 0) {
			return a;
		}

		return gcd(b, a % b);
	}

}