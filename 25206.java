// 25206.java
// 23.07.17. 04:15 ~

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		long cntTotal = 0;
		double valueTotal = 0;
		double[] grade = {4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0, 0.0};
		String[] gradeName = {"A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F", "P"};


		for (int i = 0; i < 20; i++) {
			st = new StringTokenizer(br.readLine());
			String s = st.nextToken();
			Double v = Double.parseDouble(st.nextToken());
			s = st.nextToken();

			for (int j = 0; j < 10; j++) {
				if (s.equals(gradeName[j])) {
					valueTotal += v*grade[j];
					if (j != 9) {
						cntTotal += v;
					}
					break;
				}
			}
		}
		double result = valueTotal/cntTotal;
		System.out.printf("%.6f", result);
	}
}