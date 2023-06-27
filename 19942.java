// 19942.java
// 23.06.27. 10:30 ~ 1시간반

import java.io.*;
import java.util.*;

class Main {
	static int N;
	static Item mItem;
	static Item[] items;
	static int result;
	static ArrayList<Integer> resultPath;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		items = new Item[N];
		st = new StringTokenizer(br.readLine());
		int p,f,s,v,c;

		resultPath = new ArrayList<>();

		result = 1;
		int resultCompare = 1;
		p = Integer.parseInt(st.nextToken());
		f = Integer.parseInt(st.nextToken());
		s = Integer.parseInt(st.nextToken());
		v = Integer.parseInt(st.nextToken());
		mItem = new Item(p, f, s, v, 0);
		for (int i = 0; i < N; i++){
			st = new StringTokenizer(br.readLine());
			p = Integer.parseInt(st.nextToken());
			f = Integer.parseInt(st.nextToken());
			s = Integer.parseInt(st.nextToken());
			v = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());
			items[i] = new Item(p, f, s, v, c);
			result += c;
			resultCompare += c;
		}
		for (int i = 0; i < N; i++){
			Item x = items[i];
			dfs(new Select(x.p, x.f, x.s, x.v, x.c, i, new ArrayList<Integer>()));
		}
		
		if (resultPath.isEmpty()) {
			System.out.println(-1);
		} else {
			System.out.println(result);
			for(int x : resultPath){
				System.out.print(x + 1 + " ");
			}
			System.out.println();
		}
	}

	static void dfs(Select curSelect){
		curSelect.path.add(curSelect.idx);
		if (curSelect.cA >= result){
			return;
		}
		if (varify(curSelect)){
			result = curSelect.cA;
			resultPath = curSelect.path;
			return;
		}
		for (int i = curSelect.idx + 1; i < N; i++){
			dfs(new Select(curSelect.pA + items[i].p, curSelect.fA + items[i].f, curSelect.sA + items[i].s, curSelect.vA + items[i].v, curSelect.cA + items[i].c, i, (ArrayList<Integer>)(curSelect.path).clone()));
		}
	}


	static boolean varify(Select s){
		if (s.pA < mItem.p || s.fA < mItem.f || s.sA < mItem.s || s.vA < mItem.v){
			return false;
		}
		return true;
	}

	static class Select {
		int pA, fA, sA, vA, cA;
		int idx;
		ArrayList<Integer> path;

		Select(int pA, int fA, int sA, int vA, int cA, int idx, ArrayList<Integer> path) {
			this.pA = pA;
			this.fA = fA;
			this.sA = sA;
			this.vA = vA;
			this.cA = cA;
			this.idx = idx;
			this.path = path;
		}
	}

	static class Item {
		int p;
		int f;
		int s;
		int v;
		int c;

		Item(int p, int f, int s, int v, int c) {
			this.p = p;
			this.f = f;
			this.s = s;
			this.v = v;
			this.c = c;
		}
	}
}