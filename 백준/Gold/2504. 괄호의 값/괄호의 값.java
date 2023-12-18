// 너무어렵더,,
import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		int[] cnt = new int[4];
		int result = 0;

		int k = 0;
		int tmp = 1;
		Stack<Character> stack =  new Stack<>();
		boolean flag = true;
		for (int i = 0; i < str.length(); i++) {
			if (flag == false) {
				result = 0;
				break;
			}
			switch (str.charAt(i)) {
				case '(':
					stack.push('(');
					tmp *= 2;
					break;
				case '[':
					stack.push('[');
					tmp *= 3;
					break;
				case ')':
					if (stack.isEmpty() || stack.peek() != '(') {
						flag = false;
						break;
					}
					if (str.charAt(i - 1) == '(') {
						result += tmp;
					}
					stack.pop();
					tmp /= 2;
					break;
				case ']':
					if (stack.isEmpty() || stack.peek() != '[') {
						flag = false;
						break;
					}
					if (str.charAt(i - 1) == '[') {
						result += tmp;
					}
					stack.pop();
					tmp /= 3;
					break;
			}
		}
		if (flag && stack.isEmpty()) {
			System.out.println(result);
		} else {
			System.out.println(0);
		}
	}
}