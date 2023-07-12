// 17144.java
// 23.06.14. 10:24 ~

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;
import java.util.List;

class Main {

	static int result;
	static int[][] dusts;
	static int R, C, T;
	static int[] di = {0, -1, 0, 1};
	static int[] dj = {1, 0, -1, 0};
	static int[] condi1;
	static int[] condi2;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		List<nextDust> q = new ArrayList<>();
		List<Condi> condis = new ArrayList<>();

		st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		T = Integer.parseInt(st.nextToken());
		dusts = new int[R][C];

		for (int i = 0; i < R; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < C; j++) {
				dusts[i][j] = Integer.parseInt(st.nextToken());
				if (dusts[i][j] == -1) {
					condis.add(new Condi(i, j));
				}
			}
		}
		for (; T > 0; T--) {
			for (int i = 0; i < R; i++) {
				for (int j = 0; j < C; j++) {
					if (dusts[i][j] > 0) {
						int part = dusts[i][j] / 5;
						for (int k = 0; k < 4; k++) {
							int ni = di[k] + i;
							int nj = dj[k] + j;
							if (0 <= ni && ni < R && 0 <= nj && nj < C && dusts[ni][nj] != -1) {
								q.add(new nextDust(ni, nj, part));
								dusts[i][j] -= part;
							}
						}
					}
				}
			}

			for (nextDust nextDust : q) {
				dusts[nextDust.y][nextDust.x] += nextDust.v;				
			}
			q.clear();

			int ci = condis.get(0).y - 1;
			int cj = condis.get(0).x;
			
			while (ci > 0) {
				dusts[ci][cj] = dusts[ci - 1][cj];
				ci--;
			}
			while (cj < C - 1) {
				dusts[ci][cj] = dusts[ci][cj + 1];
				cj++;
			}
			while (ci < condis.get(0).y) {
				dusts[ci][cj] = dusts[ci + 1][cj];
				System.out.println(ci + " " + cj);
				ci++;
			}
			while (cj > 1) {
				dusts[ci][cj] = dusts[ci][cj - 1];
				cj--; 
			}
			dusts[ci][cj] = 0;

			ci = condis.get(1).y + 1;
			cj = condis.get(1).x;
			
			while (ci < R - 1) {
				dusts[ci][cj] = dusts[ci + 1][cj];
				ci++;
			}
			while (cj < C - 1) {
				dusts[ci][cj] = dusts[ci][cj + 1];
				cj++;
			}
			while (ci > condis.get(1).y) {
				dusts[ci][cj] = dusts[ci - 1][cj];
				ci--;
			}
			while (cj > 1) {
				dusts[ci][cj] = dusts[ci][cj - 1];
				cj--; 
			}
			dusts[ci][cj] = 0;
		}

		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (dusts[i][j] > 0) {
					result += dusts[i][j];
				}
			}
		}
		System.out.println(result);
	}

	static class nextDust {

		int y;
		int x;
		int v;

		nextDust(int y, int x, int v) {
			this.y = y;
			this.x = x;
			this.v = v;
		}

	}

	static class Condi {
		int y;
		int x;

		Condi(int y, int x) {
			this.y = y;
			this.x = x;
		}
	}
}