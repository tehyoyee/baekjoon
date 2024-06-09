// 16926.java
// 24.03.19. 12:00 ~ 13:17

import java.util.*;
import java.io.*;

class Main {

    static int N, M, R;
    static int[][] graph;


    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        graph = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        List<Pos> startPos = new ArrayList<>();
        List<Integer> rotationList = new ArrayList<>();
        List<List<Integer>> list = new ArrayList<>();
        List<List<Pos>> stDimension = new ArrayList<>();
        int diffMax = N < M ? N : M / 2;

        for (int k = 0; k < diffMax; k++) {
            List<Integer> temp = new ArrayList<>();
            for (int i = k, j = k; i < N - 1 - k; i++) {
                temp.add(graph[i][j]);
            }
            for (int i = N - 1 - k, j = k; j < M - 1 - k; j++) {
                temp.add(graph[i][j]);
            }
            for (int i = N - 1 - k, j = M - 1 - k; i > k; i--) {
                temp.add(graph[i][j]);
            }
            for (int i = k, j = M - 1 - k; j > k; j--) {
                temp.add(graph[i][j]);
            }
            list.add(temp);
        }
        // for (int k = 0; k < diffMax; k++) {
        //     List<Pos> temp = new ArrayList<>();

        //     for (int i = 0, j = k; i < N - 1 - k * 2; i++) {
        //         temp.add(new Pos(i + k, j + k));
        //         System.out.println("1");
        //     }
        //     for (int i = N - 1 - 2 * k, j = 0; j < M; j++) {
        //         temp.add(new Pos(i, j + k));
        //         System.out.println("2");
        //     }
        //     for (int i = N - 1 - 2 * k, j = M - 1 - 2 * k; i > 0; i--) {
        //         temp.add(new Pos(i + k, j));
        //         System.out.println("3");
        //     }
        //     for (int i = 0, j = M - 1 + 2 * k; j > 0; j--) {
        //         temp.add(new Pos(i + k, j));
        //         System.out.println("4");
        //     }
        //     stDimension.add(temp);
        // }
        for (List<Integer> x : list) {
            for (Integer y : x) {
                System.out.println(y + " " );
            }
            System.out.println();
        }

        int period = (N - 1 + M - 1) * 2;
        // 주기 = (밑-1 + 높-1) * 4
        for (int i = 0; i < (N < M ? N : M)/2; i++) {
            startPos.add(new Pos(i, i));
            rotationList.add(R % period);
            period -= 8;
        }
        // for (Pos start : startPos) {
        //     System.out.println(start.x + " " +  start.y);
        // }


    }

    static class Pos {
        int y;
        int x;
        Pos(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
}