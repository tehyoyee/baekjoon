// 14940.java
// 23.07.24. 23:28 ~ 23:44

import java.io.*;
import java.util.*;

class Main {

	static int[] di = {0, 0, 1, -1};
	static int[] dj = {1, -1, 0, 0};
	static int N, M;
	static int[][] graph;
	static int[][] visit;
	static Pos start;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		graph = new int[N][M];
		visit = new int[N][M];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {

				graph[i][j] = Integer.parseInt(st.nextToken());
				if (graph[i][j] == 2) {
					start = new Pos(i, j);
				}
			}
		}

		LinkedList<Pos> q = new LinkedList<>();
		q.add(start);

		while (!q.isEmpty()) {
			Pos cPos = q.poll();
			int ci = cPos.i;
			int cj = cPos.j;

			for (int k = 0; k < 4; k++) {
				int ni = ci + di[k];
				int nj = cj + dj[k];

				if (0 <= ni && ni < N && 0 <= nj && nj < M && visit[ni][nj] == 0 && graph[ni][nj] == 1) {
					visit[ni][nj] = visit[ci][cj] + 1;
					q.add(new Pos(ni, nj));
				}
			}
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (visit[i][j] == 0 && graph[i][j] == 1) {
					System.out.print(-1 + " ");
				} else {
					System.out.print(visit[i][j] + " ");
				}
			}
			System.out.println();
		}
	}

	static class Pos {
		int i;
		int j;

		Pos(int i, int j) {
			this.i = i;
			this.j = j;
		}
	}
}