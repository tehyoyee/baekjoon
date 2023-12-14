import java.util.*;

class Solution {
    
    static int[] result;
    static Deque<Pos> q;
    static boolean[][] visit;
    static int[] di = {0, 0, -1, 1};
    static int[] dj = {1, -1, 0, 0};
    static int w, h;
    static int[][] lands;
    
    public int solution(int[][] land) {
        
        lands = land;
        w = land[0].length;
        h = land.length;
        result = new int[w];
        int resultFinal = 0;
        visit = new boolean[h][w];
        
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                bfs(i, j);
            }
        }
        for (int j = 0; j < w; j++) {
            resultFinal = Math.max(resultFinal, result[j]);
        }
        
        return resultFinal;
    }
    
    public void bfs(int i, int j) {
        if (visit[i][j] || lands[i][j] == 0) {
            return;
        }
        q = new LinkedList<>();
        visit[i][j] = true;
        q.add(new Pos(i, j));
        boolean[] candi = new boolean[w];
        candi[j] = true;
        int resultPartial = 1;
        
        while (!q.isEmpty()) {
            Pos tmp = q.poll();
            int ci = tmp.i;
            int cj = tmp.j;
            for (int k = 0; k < 4; k++) {
                int ni = ci + di[k];
                int nj = cj + dj[k];
                if (!(0 <= ni && ni < h && 0 <= nj && nj < w)
                    || visit[ni][nj] == true
                    || lands[ni][nj] == 0
                   )
                    continue;
                visit[ni][nj] = true;
                candi[nj] = true;
                q.add(new Pos(ni, nj));
                resultPartial++;
            }            
        }
        for (int k = 0; k < w; k++) {
            if (candi[k] == true)
                result[k] += resultPartial;
        }
        
    }
                    
    public static class Pos {
        int i;
        int j;

        Pos(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }
}
