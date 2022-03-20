public class takingGroupPhoto {                                         // 이번 문제는 하나의 테스트 안에 여러 개의 테케가 존재하므로 메서드 호출이전에 statci 초기화가 필요하다.
    static int answer = 0;
    static String[] arr = { "A", "C", "F", "J", "M", "N", "R", "T" };
    static String[] newData;

    public static int solution(int n, String[] data) {
        String[] output = new String[8];                                // 하나의 dfs 케이스를 담기위한 배열
        boolean[] visited = new boolean[8];                             // 해당 node의 방문여부 체크를 위한 배열 (기본 false)
        newData = data;                                                 // Input으로 받은 data => static 변수처리 (모든 지역에서 사용가능하게끔)
        answer = 0;                                                     // 정답 초기화
        permutate(output, visited, 0);                                  // permutate 메서드에 필요한 인자들을 넣고 수행 //System.out.println(answer);
        return answer;
    }

    static void permutate(String[] output, boolean[] visited, int depth) {
        if (depth == 8) {                                               // 40320 => 모든 경우의 수. 전체집합은 고정임
            isValid(output);                                            // 하나 case에 대하여 해당 case의 배열을 구했다면 검증 단계 수행
        } else {
            for (int i = 0; i < 8; i++) {
                if (visited[i] == false) {                              // 1.8명의 친구들("A", "C", "F", "J", "M", "N", "R", "T")중에 순서대로 확인해보면서 해당 케이스가 방문하지 않았다면 
                    visited[i] = true;                                  // 2.일단 해당 케이스(ex: "A")는 방문한것으로 체크해준다.
                    output[depth] = arr[i];                             // 3.방문한 친구를 출력 배열의 depth칸에 넣는다.
                    permutate(output, visited, depth + 1);              // 4."A"친구는 방문한 것으로 기록된(viited = true;)채로 다시 1,2,3번을 반복하기위해 함수자기자신을 호출해버린다.
                    visited[i] = false;                                 // 5. 다음 독립사건을 탐색하러 깊이 이동이 아닌 너비이동을 수행할때 같은 깊이 이하의 노드들에 대해서는 방문여부를 초기화해준다.
                }
            }
        }
    }

    static void isValid(String[] output) {                              // 검증 단계 -> 해당 케이스가 유효한가
        int pos1 = 0;                                                   // pos1,pos2 => 해당 조건의 두친구의 위치
        int pos2 = 0;
        for (String option : newData) {

            for (int i = 0; i < 8; i++) {
                if (output[i].equals(option.substring(0, 1))) {
                    pos1 = i;
                } else if (output[i].equals(option.substring(2, 3))) {
                    pos2 = i;
                }
            }
            int con = Integer.parseInt(option.substring(4));            // 조건의 제한거리

            if (option.substring(3, 4).equals("=") && Math.abs(pos1 - pos2) != con + 1) {       // 조건 검증 -> 해당 조건을 어겼을경우 검증을 종료
                return;
            } else if (option.substring(3, 4).equals(">") && Math.abs(pos1 - pos2) < con + 2) {
                return;
            } else if (option.substring(3, 4).equals("<") && Math.abs(pos1 - pos2) > con) {
                return;
            }
        }
        answer++;                                                       // 위의 검증 if문을 무사히 모두 통과했다면 해당 케이스는 유효하므로 count up
    }
}
