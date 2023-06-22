// 17836.java
// 23.06.22. 09:23 ~

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Queue;
import java.util.StringTokenizer;
import java.util.LinkedList;

class Main {
	static int N, M, T;
	static int[][] graph;
	static boolean[][] visit;
	static boolean[][] visit2;
	static int[] di = {0, 0, 1, -1};
	static int[] dj = {1, -1, 0, 0};

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		T = Integer.parseInt(st.nextToken());
		graph = new int[N][M];
		visit = new boolean[N][M];
		visit2 = new boolean[N][M];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		Queue<Pos> q = new LinkedList<>();

		visit[0][0] = true;
		q.add(new Pos(0, 0, false, 0));

		while (!q.isEmpty()) {
			Pos curPos = q.poll();
			int ci = curPos.i;
			int cj = curPos.j;
			boolean cw = curPos.w;
			int steps = curPos.steps;

			if (ci == N - 1 && cj == M - 1) {
				System.out.println(steps);
				return;
			}
			if (T == steps){
				continue;
			}

			for (int k = 0; k < 4; k++) {
				int ni = ci + di[k];
				int nj = cj + dj[k];

				if (!cw) {
					if (0 <= ni && ni < N && 0 <= nj && nj < M && !visit[ni][nj]) {
						if (graph[ni][nj] == 0) {
							visit[ni][nj] = true;
							q.add(new Pos(ni, nj, false, steps + 1));
						} else if (graph[ni][nj] == 2) {
							visit[ni][nj] = true;
							q.add(new Pos(ni, nj, true, steps + 1));
						}
					}
				}
				else if (0 <= ni && ni < N && 0 <= nj && nj < M && !visit2[ni][nj]) {
					visit2[ni][nj] = true;
					q.add(new Pos(ni, nj, true, steps + 1));	
				}
			}
		}
		System.out.println("Fail");
	}

	static class Pos {
		int i;
		int j;
		boolean w;
		int steps;

		Pos(int i, int j, boolean w, int steps) {
			this.i = i;
			this.j = j;
			this.w = w;
			this.steps = steps;
		}
	}
}