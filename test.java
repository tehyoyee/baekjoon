import java.util.*;


class Main {

	public static void main(String[] args) {

		ArrayList<Integer> k = new ArrayList<>();

		k.add(3);
		k.add(4);
		f(k);
		for(int x : k){
			System.out.println(x);
		}
	}

	static void f(new ArrayList<Integer> k){
		k.add(2);
	}
}
