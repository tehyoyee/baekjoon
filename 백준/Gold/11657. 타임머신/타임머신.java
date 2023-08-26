
import java.util.*;
import java.io.*;

class Main {

	static int N, M;
	static ArrayList<Bus> buses;
	static final long INF = 987654321;
	static long[] dist;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		buses = new ArrayList<Bus>();
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			buses.add(new Bus(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
		}
		dist = new long[N + 1];
		for (int i = 0; i < N + 1; i++) {
			dist[i] = INF;
		}
		if (bf(1) == true) {
			sb.append("-1\n");
		} else {
			for (int i = 2; i < N + 1; i++) {
				if (dist[i] == INF) {
					sb.append("-1\n");
				} else {
					sb.append(dist[i] + "\n");
				}
			}
		}
		System.out.print(sb);
	}

	public static Boolean bf(int start) {
		dist[1] = 0;
		for (int i = 0; i < N; i++) {
			for (Bus bus : buses) {
				int ci = bus.start;
				int ni = bus.end;
				long cost = bus.cost;

				if (dist[ci] != INF && dist[ci] + cost < dist[ni]) {
					dist[ni] = dist[ci] + cost;
					if (i == N - 1) {
						return true;
					}
				}
			}
		}
		return false;
	}

	public static class Bus {
		int start;
		int end;
		long cost;

		Bus(int start, int end, long cost) {
			this.start = start;
			this.end = end;
			this.cost = cost;
		}
	}
}