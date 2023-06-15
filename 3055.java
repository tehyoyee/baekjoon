// 3055.java
// 23.06.15. 15:43 ~ 16:43

import java.io.*;
import java.util.*;

class Main {
	static int R, C;
	static char[][] graph;
	static int[][] visit;
	static Queue<Pos> q;
	static int di[] = {1, -1, 0, 0};
	static int dj[] = {0, 0, 1, -1};
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int result = 0;
		st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		graph = new char[R][C];
		visit = new int[R][C];
		q = new LinkedList<>();
		Queue<Pos> tmpq = new LinkedList<>();

		for (int i = 0; i < R; i++) {
			st = new StringTokenizer(br.readLine());
			String s = st.nextToken();
			for (int j = 0; j < C; j++) {
				char tmp = s.charAt(j);
				if (tmp == '*') {
					tmpq.add(new Pos(i, j, Type.WATER));
					visit[i][j] = 1;
				} else if (tmp == 'S') {
					visit[i][j] = 1;
					q.add(new Pos(i, j, Type.PLAYER));
				}
				graph[i][j] = tmp;
			}
		}

		while (!tmpq.isEmpty()) {
			q.add(tmpq.poll());
		}

		while (!q.isEmpty()) {
			Pos curPos = q.poll();
			int ci = curPos.y;
			int cj = curPos.x;
			Type type =curPos.type;

			if (type == Type.PLAYER) {
				if (graph[ci][cj] == 'D') {
					result = visit[ci][cj];
					break;
				} else if (graph[ci][cj] == '*') {
					continue;
				}
			}
			for (int k = 0; k < 4; k++) {
				int ni = ci + di[k];
				int nj = cj + dj[k];
				if (0 <= ni && ni < R && 0 <= nj && nj < C) {
					if (type == Type.PLAYER) {
						if (visit[ni][nj] == 0 && graph[ni][nj] != 'X' && graph[ni][nj] != '*') {
							visit[ni][nj] = visit[ci][cj] + 1;
							q.add(new Pos(ni, nj, type));
						}
					} else {
						if (graph[ni][nj] != 'D' && graph[ni][nj] != 'X' && graph[ni][nj] != '*') {
							graph[ni][nj] = '*';
							q.add(new Pos(ni, nj, type));
						}
					}
				}
			}
		}
		if (result != 0) {
			System.out.println(result - 1);
		} else {
			System.out.println("KAKTUS");
		}
	}

	public static class Pos {
		int y;
		int x;
		Type type;

		Pos(int i, int j, Type type) {
			y = i;
			x = j;
			this.type = type;
		}
	}

	enum Type {
		WATER, PLAYER;
	}
}