import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Virus {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        int[][] arr = new int[n + 1][n + 1];
        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a][b] = arr[b][a] = 1;
        }

        Queue<Integer> q = new LinkedList<>();
        boolean[] visit = new boolean[n + 1];

        q.add(1);
        visit[1] = true;

        int count = 0;
        while (!q.isEmpty()) {
            int v = q.poll();
            for (int i = 1; i <= n; i++) {
                if (arr[v][i] == 1 && !visit[i]) {
                    visit[i] = true;
                    q.add(i);
                    count++;
                }
            }
        }
        System.out.println(count);
    }

}