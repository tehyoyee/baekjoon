// 15654.java
// 24.03.19. 11:27 ~ 11:53

import java.util.*;
import java.io.*;

class Main {

    static int N, M;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N];
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
        dfs(new ArrayList<>(), new boolean[N]);

    }

    public static void dfs(List<Integer> result, boolean[] visit) {

        if (result.size() == M) {
            for (int i = 0; i < M; i++) {
                System.out.print(result.get(i) + " ");
            }
            System.out.println();
            return;
        }

        for (int i = 0; i < N; i++) {
            if (visit[i])
                continue;
            result.add(arr[i]);
            visit[i] = true;
            dfs(result, visit);
            visit[i] = false;
            result.remove(result.size()-1);
            
        }
    }

}