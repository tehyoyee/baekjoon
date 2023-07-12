import java.io.*;
import java.util.*;

class Main {

	static int T;
	static int[] lst;
	static int L;
	static String order;
	static ArrayDeque<Integer> q;
	static boolean status;
	static StringBuilder sb;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		T = Integer.parseInt(st.nextToken());

		for (;T > 0; T--) {
			st = new StringTokenizer(br.readLine());
			q = new ArrayDeque<>();
			order = st.nextToken();
			st = new StringTokenizer(br.readLine());
			L = Integer.parseInt(st.nextToken());
			status = true;
			st = new StringTokenizer(br.readLine(), "[],");
			for (int i = 0; i < L; i++) {
				q.add(Integer.parseInt(st.nextToken()));
			}
			int flag = 1;

			for (int i = 0; i < order.length(); i++) {
				if (order.charAt(i) == 'R') {
					flag *= -1;
				} else {
					if (flag == 1) {
						if (q.poll() == null) {
							status = false;
							break;
						}
					} else {
						if (q.pollLast() == null) {
							status = false;
							break;
						}
					}
				}
			}
			if (!status) {
				System.out.println("error");
				continue;
			} else {
				sb = new StringBuilder();
				sb.append('[');
				while (!q.isEmpty()) {
					if (flag == 1) {
						sb.append(q.poll()).append(",");
					} else {
						sb.append(q.pollLast()).append(",");
					}
				}
				if (sb.length() > 2)
					sb.deleteCharAt(sb.lastIndexOf(","));
				sb.append(']');
			}
			System.out.println(sb);
		}
	}
}