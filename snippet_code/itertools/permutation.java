import java.util.Arrays;

//  DFS와 재귀를 이용하여 순열을 구해보자.

public class permutation {
    public static void main(String[] args) {
        int[] arr = { 1, 2, 3 }; // Input 배열

        int n = arr.length; // 배열의 길이

        int[] output = new int[n]; // 순열 출력을 위한 배열

        boolean[] visited = new boolean[n]; // 해당 node의 방문여부 체크를 위한 배열 (기본 false)

        permutate(arr, output, visited, 0, n, 3);

    }

    // DFS를 이용한 구현(나온 열들의 순서가 보장됨) n개 중에서 r 개를 뽑는 경우
    static void permutate(int[] arr, int[] output, boolean[] visited, int depth, int n , int r) {
        if (depth == r) {
            System.out.println(Arrays.toString(output));
        } else {
            // 1-> 2 -> 3 최하단까지 갔을 경우 모두 false 가 되므로 해당 깊이에서 해당 case의 삼중 포문중 가장 안쪽의 포문이 닫힌다.
            // -> 3 -> 2 두번째 포문의 두번째 케이스 똑같이 수행
            // 2-> 1 -> 3 ..etc

            for (int i = 0; i < n; i++) {
                if (visited[i] == false) { // 방문하지 않았다면
                    visited[i] = true; // 방문한것으로 체크해준다.
                    output[depth] = arr[i]; // 방문한 숫자를 출력 배열의 depth칸에 넣는다.
                    permutate(arr, output, visited, depth + 1, n, r); // 한층 더 내려가서 재귀로 지금까지 했던 결과값들을 기준으로 한번 더
                                                                          // 수행한다.dfs
                    visited[i] = false; // 방문여부를 초기화 해준다.
                }
            }
        }
    }
}
