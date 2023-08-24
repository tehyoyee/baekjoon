//16
import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] arr = new int[N + 1];
		for (int i = 1; i < N + 1; i++) {
			arr[i] = i + arr[i-1];
		}
		int result = 0;
		int s = 0;
		int e = 0;
		while (e <= N) {
			if (arr[e] - arr[s] == N) {
				s++;
				result++;
			} else if (arr[e] - arr[s] < N) {
				e++;
			} else {
				s++;
			}
		}
		System.out.println(result);

	}
}