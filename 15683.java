// 15683.java
// 23.06.13. 09:56 ~ 

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.LinkedList;

class Main {
	static int N, M;
	static int[][] graph;
	static List<Cctv> cctvs = new ArrayList<>();
	static int[] di = {1, -1, 0, 0, 0, -1, 0, 1, 0, -1};
	static int[] dj = {0, 0, 1, -1, 1, 0, -1, 0, 1, 0};
	static int result;
	static int space = 0;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		graph = new int[N][M];
		result = N * M;
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				int tmp = Integer.parseInt(st.nextToken());
				if (1 <= tmp && tmp <= 5) {
					cctvs.add(new Cctv(i, j, tmp));
				} else if (tmp == 0) {
					space++;
				}
				graph[i][j] = tmp;
			}
		}
		dfs(0, 0);
		System.out.println(result);
	}

	public static void dfs(int idx, int steps) {
		if (idx == cctvs.size()) {
			if (space - steps < result) {
				result = space - steps;
			}
			return;
		}
		Cctv cur = cctvs.get(idx);
		int ci = cur.y;
		int cj = cur.x;
		if (cur.type == 1) {
			for (int k = 0; k < 4; k++) {
				int l = 1;
				LinkedList<Integer> q = new LinkedList<>();
				int newSteps = 0;
				while (true) {
					int ni = ci + di[k] * l;
					int nj = cj + dj[k] * l;
					if (0 <= ni && ni < N && 0 <= nj && nj < M) {
						if (graph[ni][nj] == 6) {
							break;
						} else if (graph[ni][nj] == 0) {
							graph[ni][nj] = cur.type;
							q.add(ni);
							q.add(nj);
							newSteps++;
						}
						l++;
					} else {
						break;
					}
				}
				dfs(idx + 1, steps + newSteps);
				while (!q.isEmpty()) {
					int ni = q.getFirst();
					q.removeFirst();
					int nj = q.getFirst();
					q.removeFirst();
					graph[ni][nj] = 0;
				}
			}
		} else if (cur.type == 2) {
			int newSteps = 0;
			LinkedList<Integer> q = new LinkedList<>();
			for (int k = 0; k < 2; k++) {
				int l = 1;
				while (true) {
					int ni = ci + di[k] * l;
					int nj = cj + dj[k] * l;
					if (0 <= ni && ni < N && 0 <= nj && nj < M) {
						if (graph[ni][nj] == 6) {
							break;
						} else if (graph[ni][nj] == 0) {
							graph[ni][nj] = cur.type;
							q.add(ni);
							q.add(nj);
							newSteps++;
						}
						l++;
					} else {
						break;
					}
				}
			}
			dfs(idx + 1, steps + newSteps);
			while (!q.isEmpty()) {
				int ni = q.getFirst();
				q.removeFirst();
				int nj = q.getFirst();
				q.removeFirst();
				graph[ni][nj] = 0;
			}
			newSteps = 0;
			q = new LinkedList<>();
			for (int k = 2; k < 4; k++) {
				int l = 1;
				while (true) {
					int ni = ci + di[k] * l;
					int nj = cj + dj[k] * l;
					if (0 <= ni && ni < N && 0 <= nj && nj < M) {
						if (graph[ni][nj] == 6) {
							break;
						} else if (graph[ni][nj] == 0) {
							graph[ni][nj] = cur.type;
							q.add(ni);
							q.add(nj);
							newSteps++;
						}
						l++;
					} else {
						break;
					}
				}
			}
			dfs(idx + 1, steps + newSteps);
			while (!q.isEmpty()) {
				int ni = q.getFirst();
				q.removeFirst();
				int nj = q.getFirst();
				q.removeFirst();
				graph[ni][nj] = 0;
			}
		} else if (cur.type == 3) {
			int newSteps = 0;
			LinkedList<Integer> q = new LinkedList<>();
			for (int i = 0; i < 4; i++) {
				newSteps = 0;
				for (int k = 4 + i; k < 4 + i + 2; k++) {
					int l = 1;
					while (true) {
						int ni = ci + di[k] * l;
						int nj = cj + dj[k] * l;
						if (0 <= ni && ni < N && 0 <= nj && nj < M) {
							if (graph[ni][nj] == 6) {
								break;
							} else if (graph[ni][nj] == 0) {
								graph[ni][nj] = cur.type;
								q.add(ni);
								q.add(nj);
								newSteps++;
							}
							l++;
						} else {
							break;
						}
					}
				}
				dfs(idx + 1, steps + newSteps);
				while (!q.isEmpty()) {
					int ni = q.getFirst();
					q.removeFirst();
					int nj = q.getFirst();
					q.removeFirst();
					graph[ni][nj] = 0;
				}
			}
		} else if (cur.type == 4) {
			int newSteps = 0;
			LinkedList<Integer> q = new LinkedList<>();
			for (int i = 0; i < 4; i++) {
				newSteps = 0;
				for (int k = 4 + i; k < 4 + i + 3; k++) {
					int l = 1;
					while (true) {
						int ni = ci + di[k] * l;
						int nj = cj + dj[k] * l;
						if (0 <= ni && ni < N && 0 <= nj && nj < M) {
							if (graph[ni][nj] == 6) {
								break;
							} else if (graph[ni][nj] == 0) {
								graph[ni][nj] = cur.type;
								q.add(ni);
								q.add(nj);
								newSteps++;
							}
							l++;
						} else {
							break;
						}
					}
				}
				dfs(idx + 1, steps + newSteps);
				while (!q.isEmpty()) {
					int ni = q.getFirst();
					q.removeFirst();
					int nj = q.getFirst();
					q.removeFirst();
					graph[ni][nj] = 0;
				}
			}
		} else if (cur.type == 5) {
			int newSteps = 0;
			LinkedList<Integer> q = new LinkedList<>();
			for (int k = 0; k < 4; k++) {
				int l = 1;
				while (true) {
					int ni = ci + di[k] * l;
					int nj = cj + dj[k] * l;
					if (0 <= ni && ni < N && 0 <= nj && nj < M) {
						if (graph[ni][nj] == 6) {
							break;
						} else if (graph[ni][nj] == 0) {
							graph[ni][nj] = cur.type;
							q.add(ni);
							q.add(nj);
							newSteps++;
						}
						l++;
					} else {
						break;
					}
				}
			}
			dfs(idx + 1, steps + newSteps);
			while (!q.isEmpty()) {
				int ni = q.getFirst();
				q.removeFirst();
				int nj = q.getFirst();
				q.removeFirst();
				graph[ni][nj] = 0;
			}
		}
	}

	public static class Cctv {

		int type;
		int y;
		int x;

		Cctv(int i, int j, int type) {
			this.y = i;
			this.x = j;
			this.type = type;
		}

	}

}


