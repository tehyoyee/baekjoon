// 7785.java
// 23.08.07. 10:40 ~ 10:52

import java.util.*;
import java.io.*;

class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		HashMap<String, String> hashMap = new HashMap<>();

		int n = Integer.parseInt(br.readLine());
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			String employee;
			String status;

			employee = st.nextToken();
			status = st.nextToken();
			if (status.equals("enter")) {
				hashMap.put(employee, status);
			} else if (hashMap.containsKey(employee)) {
				hashMap.remove(employee);
			}
		}
	
		ArrayList<String> arrayList = new ArrayList<>(hashMap.keySet());
		Collections.sort(arrayList, Collections.reverseOrder());
		for (String x : arrayList) {
			sb.append(x).append("\n");
		}
		System.out.print(sb);
	}
}