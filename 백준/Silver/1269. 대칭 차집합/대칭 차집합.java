//6
import java.io.*;
import java.util.*;

class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int intersection = 0;
		HashMap<Integer, Boolean> map = new HashMap<>();
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			map.put(Integer.parseInt(st.nextToken()), true);
		}
		st = new StringTokenizer(br.readLine());
		for (int j = 0 ; j < M; j++) {
			if (map.containsKey(Integer.parseInt(st.nextToken()))) {
				intersection++;
			}
		}
		System.out.println(N + M - intersection * 2);
	}
}