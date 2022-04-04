import java.util.*;

public class Main {
    static final int MAX_N = 10;    // Node의 최대 값
    static int N, E;    // Node와 Edge
    static int [][] Graph = new int [MAX_N][MAX_N]; // Node와 Edge를 가지고 2차원 배열에 연결상태 정보 저장
    static boolean[] visited = new boolean[MAX_N]; // 각각의 Node에 대한 방문 여부

    static void dfs (int node) {
        Visited[node] = true;       // 들어 온 값에 대하여 방문한 것으로 처리
        System.out.println(node + " "); // 출력 (값 대입)

        for (int next = 0; next < N; ++next) {      // 모든 노드에 대하여 
            if(!Visited[next] && Graph[node][next] != 0)    // 방문하지 않았고, 현재 node와 연결되어있다면
            dfs(next);  // 그 밑의 노드로 들어간다.
        }
    }

    public static void main (String[] args){    
        Scanner sc = new Scanner(System.in);    // 입력
        N = sc.nextInt();   // 노드 갯수 입력
        E = sc.nextInt();   // 간선 갯수 입력

        for (int i = 0 ; i < E ; ++i) {
            int u = sc.nextInt();   // 연결 정보 입력
            int v = sc.nextInt();
            Grapth[u][v] = Graph[v][u] = 1; // 2차원 연결 정보 공간에 연결되어있다고 입력
        }
        dfs(0); // 출발점부터 탐색시작!
    }
}