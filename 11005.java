// 11005.java
// 23.07.15. 02:51

import java.util.*;
import java.io.*;

// class Main {

// 	public static void main(String[] args) throws IOException {

// 		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
// 		StringTokenizer st = new StringTokenizer(br.readLine());

// 		int N = Integer.parseInt(st.nextToken());
// 		int B = Integer.parseInt(st.nextToken());

// 		String result = "";
// 		while (N > 0) {
// 			int tmp = N % B;
// 			if (tmp >= 10) {
// 				result = (char)(tmp - 10 + 'A') + result;
// 			} else {
// 				result = (char)(tmp + '0') + result;
// 			}
// 			N /= B;
// 		}
// 		System.out.println(result);
// 	}
// }

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());
		System.out.println(Integer.toString(N, B).toUpperCase());
	}
}
		
