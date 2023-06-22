// 2138.java
// 23.06.22. 15:34 ~

import java.util.Arrays;
import java.util.Scanner;

class Main {
	static int N;
	static int[] input;
	static int[] target;
	static int result;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		N = Integer.parseInt(sc.nextLine());
		input = new int[N];
		target = new int[N];

		String tmp = sc.nextLine();
		for (int i = 0; i < N; i++) {
			input[i] = Character.getNumericValue(tmp.charAt(i));
		}
		tmp = sc.nextLine();
		for (int i = 0; i < N; i++) {
			target[i] = Character.getNumericValue(tmp.charAt(i));
		}
		int i = 0;
		while (i < N) {
			System.out.println(i);
			if (input[i] != target[i]) {
				result++;
				input[i] = (input[i] + 1) % 2;
				if (i == 0) {
					input[i + 1] = (input[i + 1] + 1) % 2;
					i++;
				} else if (i == N - 1) {
					input[i - 1] = (input[i - 1] + 1) % 2;
					i--;
				} else {
					input[i + 1] = (input[i + 1] + 1) % 2;
					input[i - 1] = (input[i - 1] + 1) % 2;
					i--;
				}
			} else {
				i++;
			}

		}
		if (Arrays.equals(input, target)) {
			System.out.println(result);
		} else {
			System.out.println(-1);
		}
		sc.close();
	}

	static class Pos {
		int idx;
		int v;
	}
}