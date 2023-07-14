// 10989.java
// 23.07.15. 01:15

import java.io.*;
import java.util.StringTokenizer;

class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();

		int N = Integer.parseInt(st.nextToken());
		int[] visit = new int[10001];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			visit[Integer.parseInt(st.nextToken())]++;
		}
		
		for (int i = 1; i < 10001; i++) {
			for (int j = 0; j < visit[i]; j++)
				sb.append(i).append('\n');
		}
		System.out.println(sb);
	}
}