// 1707.java
// 23.06.12. 10:54 ~ 

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {

	static int T;
	static int V, E;
	static int[] visit;
	static Node[] node;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		T = Integer.parseInt(st.nextToken());

		while (T != 0) {
			st = new StringTokenizer(br.readLine());
			V = Integer.parseInt(st.nextToken());
			E = Integer.parseInt(st.nextToken());
			node = new Node[V + 1];

			for (int i = 1; i <= V; i++) {
				node[i] = new Node(i);
			}

			for (int i = 1; i <= E; i++) {
				int s;
				int e;
				st = new StringTokenizer(br.readLine());
				s = Integer.parseInt(st.nextToken());
				e = Integer.parseInt(st.nextToken());
				node[s].next.add(e);
				node[e].next.add(s);
			}
	
			boolean flag = true;
			for (int ci = 1; ci <= V; ci++) {
				LinkedList<Node> q = new LinkedList<>();
				if (node[ci].color == -1) {
					node[ci].color = 0;
					q.add(node[ci]);
				}
				while (!q.isEmpty() && flag) {
					Node curNode = q.getFirst();
					System.out.println(curNode.idx + " " + curNode.color);
					q.removeFirst();
					for (int i = 0; i < curNode.next.size(); i++) {
						Node nextNode = node[curNode.next.get(i)];
						System.out.println("next" + nextNode.idx + " " + nextNode.color);
						if (curNode.color == nextNode.color) {
							System.out.println("NO");
							flag = false;
							break;
						} else if (nextNode.color == -1) {
							nextNode.color = (curNode.color + 1) % 2;
							q.add(nextNode);
						}
					}
				}
			}
			if (flag) {
				System.out.println("YES");
			}
			--T;
		}
	}

	static class Node {
		int idx;
		int color;
		List<Integer> next = new ArrayList<>();

		Node(int idx) {
			this.idx = idx;
			this.color = -1;
		}
	}
}
