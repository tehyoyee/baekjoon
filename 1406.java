// 1406.java
// 23.07.15. 20:12 ~

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		Stack<Character> stackA = new Stack<>();
		Stack<Character> stackB = new Stack<>();

		String str = st.nextToken();
		for (int i = 0; i < str.length(); i++) {
			stackA.add(str.charAt(i));
		}

		st = new StringTokenizer(br.readLine());
		int M = Integer.parseInt(st.nextToken());

		for (int i = 0; i < M; i++) {
			String cmd = br.readLine();
			char c = cmd.charAt(0);
			if (c == 'P') {
				char element = cmd.charAt(2);
				stackA.add(element);
			} else if (c == 'L') {
				if (!stackA.isEmpty()) {
					stackB.add(stackA.pop());
				}
			} else if (c == 'D') {
				if (!stackB.isEmpty()) {
					stackA.add(stackB.pop());
				}
			} else if (c == 'B') {
				if (!stackA.isEmpty()) {
					stackA.pop();
				}
			}
		}
		while (!stackA.isEmpty()) {
			stackB.add(stackA.pop());
		}
		while (!stackB.isEmpty()) {
			bw.write(stackB.pop());
		}
		bw.flush();
		bw.close();
	}
}