// 7453.java
// 23.11.09. 8:31 ~

import java.util.*;
import java.io.*;

class Main {

	static int N;
	static int[][] arr;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int N = Integer.parseInt(br.readLine());
		arr = new int[4][N];
		for (int j = 0; j < N; j++) {
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < 4; i++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		int[] AB = new int[N*N];
		int[] CD = new int[N*N];
		for (int k = 0, i = 0; i < N; i++) {
			for (int j = 0; j < N; k++, j++) {
				AB[k] = arr[0][i] + arr[1][j];
				CD[k] = arr[2][i] + arr[3][j];
			}
		}
		Arrays.sort(AB);
		Arrays.sort(CD);

		long result = 0;
		int s = 0, e = N*N-1;
		while (0 <= s && s < N * N && 0 <= e && e < N * N) {
			int criterion = AB[s] + CD[e];
			if (criterion < 0) {
				s++;
				continue;
			}
			if (criterion > 0) {
				e--;
				continue;
			}
			int a = 1, b = 1;
			while (s < N*N-1 && AB[s] == AB[++s]) {
				a++;
			}
			while (0 <= e && CD[e] == CD[--e]) {
				b++;
			}
			result += a * b;
		}

		System.out.println(result);
	}
}


// import java.util.*;
// import java.io.*;

// class Main {

// 	static int N;
// 	static int[][] arr;

// 	public static void main(String[] args) throws IOException {

// 		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
// 		StringTokenizer st;

// 		int N = Integer.parseInt(br.readLine());
// 		arr = new int[4][N];
// 		for (int i = 0; i < N; i++) {
// 			st = new StringTokenizer(br.readLine());
// 			for (int j = 0; j < 4; j++) {
// 				arr[j][i] = Integer.parseInt(st.nextToken());
// 			}
// 		}

// 		HashMap<Integer, Integer> map1 = new HashMap<>();

// 		for (int i = 0; i < N; i++) {
// 			for (int j = 0; j < N; j++) {
// 				int s = arr[0][i] + arr[1][j];
// 				if (map1.containsKey(s)) {
// 					map1.put(s, map1.get(s) + 1);
// 				} else {
// 					map1.put(s, 1);
// 				}
// 			}
// 		}
// 		int result = 0;
// 		for (int i = 0; i < N; i++) {
// 			for (int j = 0; j < N; j++) {
// 				int s = arr[2][i] + arr[3][j];
// 				if (map1.containsKey(-s)) {
// 					result += map1.get(-s);
// 				}
// 			}
// 		}
// 		System.out.println(result);
// 	}
// }