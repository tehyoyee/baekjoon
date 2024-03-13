// 1052.java
// 24.03.13. 11:33 ~ 12:16

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {

    static int N, K;
    static int result;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        List<Integer> lst = new ArrayList<>();
        lst.add(1);
        for (int i = 0; i < 24; i++) {
            lst.add(lst.get(i)*2);
        }

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        result = 0;
        
        for (int i = 0; i < K - 1; i++) {
            for (int j = lst.size() - 1; j >= 0; j--) {
                if (lst.get(j) < N) {
                    N -= lst.get(j);
                    break;
                }
            }
        }
        for (int i = 0; i < lst.size(); i++) {
            if (lst.get(i) >= N) {
                System.out.println(lst.get(i) - N);
                System.exit(0);
            }
        }
        System.out.println(-1);
    }

}

