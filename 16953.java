// 16953.java
// 24.03.18. 23:29 ~ 23:42

import java.util.*;
import java.io.*;

class Main {
    
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Long a = Long.parseLong(st.nextToken());
        Long b = Long.parseLong(st.nextToken());
        Long result = -1L;
        Queue<X> q = new LinkedList<>();
        q.add(new X(a, 0L));

        while (!q.isEmpty()) {
            X curX = q.poll();
            Long cur = curX.x;
            Long cnt = curX.cnt;
            System.out.println(cur);

            if (cur.equals(b)) {
                result = cnt + 1;
                break;
            }
            if (cur * 10 + 1 <= b)
                q.add(new X(cur * 10 + 1, cnt + 1));
            if (cur * 2 <= b)
                q.add(new X(cur * 2, cnt + 1));
        }
        System.out.println(result);
    }
    
    static class X {
        Long x;
        Long cnt;

        X (Long x, Long cnt) {
            this.x = x;
            this.cnt = cnt;
        }
    }

}
