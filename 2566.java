// 2566.java
// 23.07.15. 01:03

import java.util.*;

class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);

		// int[][] arr = new int[10][10];
		int result = 0;
		int[] pos = new int[]{0, 0};
		for (int i = 1; i < 10; i++) {
			for (int j = 1; j < 10; j++) {
				int tmp = sc.nextInt();
				if (result < tmp) {
					pos[0] = i;
					pos[1] = j;
					result = tmp;
				}
			}
		}
		System.out.println(result);
		System.out.println(pos[0] + " " + pos[1]);
	}
}