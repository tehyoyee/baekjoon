// 7576.java

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

	static int [] di = {0, 0, 1, -1};
	static int [] dj = {1, -1, 0, 0};
	static int w, h;
	static int [][] visit;:
	static int [][] graph;
	static int day = 0;
	static Queue<Tomato> q = new LinkedList<>();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		st = new StringTokenizer(br.readLine());
		w = Integer.parseInt(st.nextToken());
		h = Integer.parseInt(st.nextToken());
		graph = new int[h][w];
		visit = new int[h][w];
		for (int i = 0; i < h; i++) {
			Arrays.fill(visit[i], -1);
		}

		for (int i = 0; i < h; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < w; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
				if (graph[i][j] == 1) {
					q.offer(new Tomato(i, j));
					visit[i][j] = 0;
				}
			}
		}
		
		while (!q.isEmpty()) {
			Tomato cur = q.poll();
			int ci = cur.i;
			int cj = cur.j;
			day = visit[ci][cj];

			for (int k = 0; k < 4; k++) {
				int ni = ci + di[k];
				int nj = cj + dj[k];
				if (0 <= ni && ni < h && 0 <= nj && nj < w) {
					if (graph[ni][nj] == 0 && visit[ni][nj] == -1) {
						visit[ni][nj] = visit[ci][cj] + 1;
						q.offer(new Tomato(ni, nj));
					}
				}
			}
		}

		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				if (visit[i][j] == -1 && graph[i][j] == 0) {
					System.out.println(-1);
					return;
				}
			}
		}
		System.out.println(day);
	}
}
class Tomato {
	int i;
	int j;

	Tomato(int i, int j) {
		this.i = i;
		this.j = j;
	}
}
