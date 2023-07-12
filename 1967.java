// 1967.java
// 23.06.14. 40분

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Queue;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.List;
import java.util.LinkedList;

class Main {
	static Pos[] graph; 
	static int[] visit;
	static int n;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken());
		graph = new Pos[n + 1];
		for (int i = 1; i < n + 1; i++) {
			graph[i] = new Pos(i);
		}

		for (int i = 0; i < n - 1; i++) {
			st = new StringTokenizer(br.readLine());
			int a, b, c;
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());

			graph[a].next.add(b);
			graph[b].next.add(a);
			graph[a].weight.add(c);
			graph[b].weight.add(c);
		}

		int start = bfs(1);
		int end = bfs(start);

		System.out.println(visit[end] - 1);
	}

	public static int bfs(int start) {
		int index = 0;
		int result = 0;
		Queue<Pos> q = new LinkedList<>();
		visit = new int[n + 1];
		visit[start] = 1;

		q.add(graph[start]);
		
		while (!q.isEmpty()) {
			Pos curPos = q.poll();
			if (visit[curPos.prev] > result) {
				result = visit[curPos.prev];
				index = curPos.prev;
			}
			for (int i = 0; i < curPos.next.size(); i++) {
				if (visit[curPos.next.get(i)] == 0) {
					visit[curPos.next.get(i)] = visit[curPos.prev] + curPos.weight.get(i);
					q.add(graph[curPos.next.get(i)]);
				}
			}
		}

		return index;
	}

	static class Pos {
		int prev;
		List<Integer> next;
		List<Integer> weight;

		Pos(int i) {
			prev = i;
			next = new ArrayList<>();
			weight = new ArrayList<>();
		}
	}
}