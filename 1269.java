// 1269.java
// 23.08.24. 15:18 ~ 15:24

/**
 * HashMap 과 HashSet
 * 두 클래스 모두 시간이 똑같게 나왔다.
 */

// import java.io.*;
// import java.util.*;

// class Main {

// 	public static void main(String[] args) throws IOException {

// 		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
// 		StringTokenizer st = new StringTokenizer(br.readLine());

// 		int N = Integer.parseInt(st.nextToken());
// 		int M = Integer.parseInt(st.nextToken());
// 		int intersection = 0;
// 		HashMap<Integer, Boolean> map = new HashMap<>();
// 		st = new StringTokenizer(br.readLine());
// 		for (int i = 0; i < N; i++) {
// 			map.put(Integer.parseInt(st.nextToken()), true);
// 		}
// 		st = new StringTokenizer(br.readLine());
// 		for (int j = 0 ; j < M; j++) {
// 			if (map.containsKey(Integer.parseInt(st.nextToken()))) {
// 				intersection++;
// 			}
// 		}
// 		System.out.println(N + M - intersection * 2);
// 	}
// }


import java.io.*;
import java.util.*;

class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int intersection = 0;
		HashSet<Integer> set = new HashSet<>();
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			set.add(Integer.parseInt(st.nextToken()));
		}
		st = new StringTokenizer(br.readLine());
		for (int j = 0 ; j < M; j++) {
			if (set.contains(Integer.parseInt(st.nextToken()))) {
				intersection++;
			}
		}
		System.out.println(N + M - intersection * 2);
	}
}