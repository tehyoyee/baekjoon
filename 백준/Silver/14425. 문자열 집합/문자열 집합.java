//6
import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int result = 0;
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		HashMap<String, Boolean> map = new HashMap<>();

		for (int i = 0; i < N; i++) {
			map.put(br.readLine(), true);
		}
		for (int i = 0; i < M; i++) {
			if (map.containsKey(br.readLine())) {
				result++;
			}
		}
		System.out.println(result);
	}
}