// 17135.java
// 23.11.01. 09:55 ~ 11:18 11:35 ~ 12:05

import java.util.*;
import java.io.*;

class Main {

	static int N, M, D;
	static int[] di = {0, -1, 0};
	static int[] dj = {-1, 0, 1};

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int result = 0;

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		D = Integer.parseInt(st.nextToken());
		int[][] graph = new int[N+1][M];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		for (int i = 0; i < M - 2; i++) {
			for (int j = i + 1; j < M - 1; j++) {
				for (int k = j + 1; k < M; k++) {
					Archers[] archers = {
						new Archers(N, i), new Archers(N, j), new Archers(N, k)
					};
					int[][] graphCopy = new int[N+1][M];
					for (int l = 0; l < N; l++) {
						graphCopy[l] = Arrays.copyOf(graph[l], M);
					}
					result = Math.max(simulate(graphCopy, archers), result);
				}
			}
		}
		System.out.println(result);
	}

	public static int simulate(int[][] graphCopy, Archers[] archers) {
		int result = 0;

		for (int t = N; t > 0; t--) {
			ArrayList<Pos> eliminatings = new ArrayList<>();
			for (int i = 0; i < 3; i++) {
				Pos tmp = bfs(graphCopy, t, archers[i].cj);
				if (tmp != null) {
					eliminatings.add(tmp);
				}
			}
			for (Pos eliminatingPos : eliminatings) {
				if (graphCopy[eliminatingPos.i][eliminatingPos.j] == 1) {
					graphCopy[eliminatingPos.i][eliminatingPos.j] = 0;
					result++;
				}
			}
		}
		return result;
	}

	public static class Archers {
		int ci;
		int cj;

		Archers(int ci, int cj) {
			this.ci = ci;
			this.cj = cj;
		}
	}

	public static Pos bfs(int[][] graphCopy, int si, int sj) {
		LinkedList<Pos> lst = new LinkedList<>();
		lst.add(new Pos(si, sj, 1));
		boolean[][] visit = new boolean[N][M];

		while (!lst.isEmpty()) {
			Pos curPos = lst.poll();
			int ci = curPos.i;
			int cj = curPos.j;
			int cs = curPos.steps;
			if (cs > D) {
				continue;
			}

			for (int k = 0; k < 3; k++) {
				int ni = ci + di[k];
				int nj = cj + dj[k];
				if (!(0 <= ni && ni < si) || !(0 <= nj && nj < M) || visit[ni][nj]) {
					continue;
				}
				if (graphCopy[ni][nj] == 1) {
					return new Pos(ni, nj, 0);
				}
				visit[ni][nj] = true;
				lst.add(new Pos(ni, nj, cs + 1));
			}
		}
		return null;
	}

	public static class Pos {
		int i;
		int j;
		int steps;

		Pos(int i, int j, int steps) {
			this.i = i;
			this.j = j;
			this.steps = steps;
		}
	}

}