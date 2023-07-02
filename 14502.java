import java.util.*;
import java.io.*;

class Main {

	static int N, M;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int[][] graph;
		ArrayList<int[2]> virus = new ArrayList<>();
		ArrayList<int[2]> candi = new ArrayList<>();
		

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		graph = new int[N][M];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
				if (graph[i][j] == '2') {
					virus.add({i, j})
				}
			}
		}

		for (int i; i)

		
	}
}