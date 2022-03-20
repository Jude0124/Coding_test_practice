public class takingGroupPhoto {
    static int answer = 0;
    static String[] arr = { "A", "C", "F", "J", "M", "N", "R", "T" };

    public static void main(String[] args) { // 테케
        solution(2, new String[] { "N~F=0", "R~T>2" });
        solution(2,new String [] {"M~C<2", "C~M>1"});

    }

    public static int solution(int n, String[] data) {
        // isValid(new String[] { "A", "C", "F", "J", "M", "N", "R", "T" }, new String[] { "N~F=0", "R~T>2" });
        String[] output = new String[8];
        boolean[] visited = new boolean[8]; // 해당 node의 방문여부 체크를 위한 배열 (기본 false)
        answer = 0;
        permutate(output, visited, 0, data);
        System.out.println(answer);
        return answer;
    }

    // DFS를 이용한 구현(나온 열들의 순서가 보장됨) n개 중에서 r 개를 뽑는 경우
    static void permutate(String[] output, boolean[] visited, int depth, String[] data) {
        if (depth == 8) { // 40320
            isValid(output, data);

        } else {

            for (int i = 0; i < 8; i++) {
                if (visited[i] == false) { // 방문하지 않았다면
                    visited[i] = true; // 방문한것으로 체크해준다.
                    output[depth] = arr[i]; // 방문한 숫자를 출력 배열의 depth칸에 넣는다.
                    permutate(output, visited, depth + 1, data); // 한층 더 내려가서 재귀로 지금까지 했던 결과값들을 기준으로 한번 더
                                                                 // 수행한다.dfs
                    visited[i] = false; // 방문여부를 초기화 해준다.
                }
            }
        }
    }

    static void isValid(String[] output, String[] data) {
        int pos1 = 0;
        int pos2 = 0;
        for (String option : data) {

            for (int i = 0; i < 8; i++) { 
                if (output[i].equals(option.substring(0, 1))) {
                    pos1 = i;
                } else if (output[i].equals(option.substring(2, 3))) {
                    pos2 = i;
                    
                }
            }
            int con = Integer.parseInt(option.substring(4));
            if (option.substring(3, 4).equals("=") && Math.abs(pos1 - pos2) !=con+1) {
                return;
            } else if (option.substring(3, 4).equals(">")
                    && Math.abs(pos1 - pos2) < con + 2) {
                return;
            } else if (option.substring(3, 4).equals("<")
                    && Math.abs(pos1 - pos2) > con) {
                return;
            }
        
        }
        answer++;
    }

}
