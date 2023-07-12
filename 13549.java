// 13549.java

import java.io.IOException;
import java.util.*;

class Main {

	static int[] visit;
	public static void main(String[] args) throws IOException {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		sc.close();
		visit = new int[100001];
		Queue<Pos> q = new LinkedList<>();
		q.add(new Pos(N, 1));
		visit[N] = 1;

		while (!q.isEmpty()) {
			Pos tmp = q.poll();
			int ci = tmp.x;
			int steps = tmp.steps;
			
			if (0 <= ci - 1 && (visit[ci - 1] == 0 || visit[ci - 1] > steps + 1)) {
				visit[ci - 1] = steps + 1;
				q.add(new Pos(ci - 1, steps + 1));
			}
			if (ci + 1 <= 100000 && (visit[ci + 1] == 0 || visit[ci + 1] > steps + 1)) {
				visit[ci + 1] = steps + 1;
				q.add(new Pos(ci + 1, steps + 1));
			}
			if (2 * ci <= 100000 && (visit[2 * ci] == 0 || visit[2 * ci] > steps)) {
				visit[2 * ci] = steps;
				q.add(new Pos(2 * ci, steps));
			}
		}
		System.out.println(visit[K] - 1);
	}

	static class Pos {
		int x;
		int steps;

		Pos(int x, int steps) {
			this.x = x;
			this.steps = steps;
		}
	}
}