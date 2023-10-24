// 11725.java
// 23.10.24. 10:47 ~

import java.util.*;
import java.io.*;

class Main {

	static int[] nodes;
	static ArrayList<ArrayList<Integer>> graph;
	static int N;
	static boolean[] visit;
	static int[] root;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
 		root = new int[N + 1];
		visit = new boolean[N + 1];
		for (int i = 0; i <= N; i++) {
			root[i] = i;
		}
		graph = new ArrayList<>();
		for (int i = 0; i <= N; i++) {
			graph.add(new ArrayList<>());
		}

		for (int i = 0; i < N-1; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());

			graph.get(a).add(b);
			graph.get(b).add(a);
		}

		Queue<Integer> q = new LinkedList<>();
		q.add(1);
		visit[1] = true;
		while (!q.isEmpty()) {
			int ci = q.poll();
			for (int ni : graph.get(ci)) {
				if (!visit[ni]) {
					visit[ni] = true;
					q.add(ni);
					root[ni] = ci;
				}
			}
		}
		StringBuilder sb = new StringBuilder();
		for (int i = 2; i <= N; i++) {
			sb.append(root[i] + " ");
		}
		System.out.println(sb);
	}

}