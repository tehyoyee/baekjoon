// 1083.java

import java.util.*;
import java.io.*;

class Main {
	
	static int N, S;
	static ArrayList<Integer> lst;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		lst = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			lst.add(Integer.parseInt(st.nextToken()));
		}
		st = new StringTokenizer(br.readLine());
		S = Integer.parseInt(st.nextToken());

		for (int i = 0; i < N - 1; i++) {
			int target = lst[i];
			int targetIdx = i;
			for (int j = i + 1; j < N; j++) {
				if (j - i > S){
					break;
				}
				if (lst[i] < lst[j]) {
					target = lst[j];
					targetIdx = j;
				}
			}
			S -= (targetIdx - i);
			lst.remove(target);
			lst.add(i, target);
		}
	}
}