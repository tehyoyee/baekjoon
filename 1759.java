import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {

	static int L, C;

	static char[] arr;
	static char[] code;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		st = new StringTokenizer(br.readLine());

		L = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());

		arr = new char[C];
		code = new char[L];
		st = new StringTokenizer(br.readLine());

		for (int i = 0; i < C; i++) {
			arr[i] = st.nextToken().charAt(0);
		}
		Arrays.sort(arr);
		dfs(0, 0);
	}

	public static void dfs(int ci, int idx) {
		if (idx == L) {
			if (isValid(code)) {
				System.out.println(code);
			}
			return;
		}
		else {
			for (int ni = ci; ni < C; ni++) {
				code[idx] = arr[ni];
				dfs(ni + 1, idx + 1);
			}
		}
	}
	
	public static boolean isValid(char[] code) {
		int consonant = 0;
		int vowel = 0;
		for (char x : code) {
			if (x == 'a' || x == 'e' || x == 'i' || x == 'o' || x == 'u') {
				vowel++;
			} else {
				consonant++;
			}			
		}
		if (consonant >= 2 && vowel >= 1) {
			return true;
		} else {
			return false;
		}
	}
}