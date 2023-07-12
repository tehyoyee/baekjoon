// 27172.java
// 23.06.07. 07:24 ~

import java.util.*;
import java.io.*;
import java.io.BufferedReader;

class Main {

	static int[] players;
	static int[] points;
	static boolean prime[] = new boolean[1000001];


	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		players = new int[N];
		points = new int[N];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			players[i] = Integer.parseInt(st.nextToken());
		}
		int K = 1000001;
        
		prime[0] = prime[1] = true;
		for(int i = 2; i*i < K; i++){
			if(!prime[i]) {
				for (int j = i*i; j < K; j += i)
					prime[j] = true;                
			}        
		}

		for (int i = 0; i < N - 1; i++) {
			for (int j = i + 1; j < N; j++) {
				if (!prime[i] && !prime[j]) {
					continue;
				} else if (players[i] % players[j] == 0) {
					--points[i];
					++points[j];
				} else if (players[j] % players[i] == 0) {
					--points[j];
					++points[i];
				}
			}
		}
		for (int x : points) {
			System.out.println(x);
		}
	}
}