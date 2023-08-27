//12
import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] arr = new int[10];
		String str = br.readLine();
		for (int i = 0; i < 10; i++) {
			arr[i] = 0;
		}

		for (int i = 0; i < str.length(); i++) {
			arr[Character.getNumericValue(str.charAt(i))]++;
		}
		int maxV = 0;
		for (int i = 0; i < 9; i++) {
			if (i == 6 || i == 9) {
				if (arr[6] + arr[9] > maxV) {
					maxV = (arr[6] + arr[9] + 1)/2;
				}
			} else if (maxV < arr[i]) {
				maxV = arr[i];
			}
		}
		System.out.println(maxV);
	}
}