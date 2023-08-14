// 12891.java
// 23.08.14. 10:46 ~ 11:15

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int result = 0;
		st = new StringTokenizer(br.readLine());
		int strLen = Integer.parseInt(st.nextToken());
		int s = 0;
		char[] charLst = {'A', 'C', 'G', 'T'};
		int e = Integer.parseInt(st.nextToken());
		String str = br.readLine();
		int[] target = new int[4];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < 4; i++) {
			target[i] = Integer.parseInt(st.nextToken());
		}
		int[] arr = new int[4];
		for (int i = 0; i < e; i++) {
			if (str.charAt(i)=='A') {
				arr[0]++;
			} else if (str.charAt(i)=='C') {
				arr[1]++;
			} else if (str.charAt(i)=='G') {
				arr[2]++;
			} else {
				arr[3]++;
			}
		}
		int flag = 1;
		for (int i = 0; i < 4; i++) {
			if (arr[i] < target[i]) {
				flag = 0;
				break;
			}
		}
		if (flag == 1) {
			result++;
		}
		for (; e < strLen; e++, s++) {
			arr[getIdx(str.charAt(s))]--;
			arr[getIdx(str.charAt(e))]++;
			if (isOk(arr, target)) {
				result++;
			}
		}
		System.out.println(result);
	}

	static int getIdx(char a) {
		if (a == 'A') {
			return 0;
		} else if (a == 'C') {
			return 1;
		} else if (a == 'G') {
			return 2;
		}
		return 3;
	}

	static boolean isOk(int[] arr, int[] target) {
		for (int i = 0; i < 4; i++) {
			if (arr[i] < target[i]) {
				return false;
			}
		}
		return true;
	}
}