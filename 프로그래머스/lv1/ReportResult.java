import java.util.*;

public class ReportResult {
    public int[] solution(String[] id_list, String[] report, int k) {

        Map<String, myObject> reportLog = new HashMap<>(); // key = 사용자 아이디, value = [신고받은횟수,사용자를 신고한 사람의 명단]

        ArrayList<Integer> preAns = new ArrayList<>();

        HashSet<String> report2 = new HashSet<>(Arrays.asList(report));

        String[] repoLast = report2.toArray(new String[0]); // 빈 딕셔너리 생성
        for (String key : id_list){
            reportLog.put(key, new myObject());
        }

        for (String repo : repoLast){                       //신고한 사람목록과 횟수 기입
            String[] temp = repo.split(" ");
            reportLog.get(temp[0]).repoTimes++;
            reportLog.get(temp[0]).reporter.add(temp[1]);

        }

        for(String key : id_list){                          // 조회하면서 해당 사용자가 받아야할 메일 수를 cnt변수로 산출
            int cnt = 0;
            for(String value2: reportLog.get(key).reporter){
                if (reportLog.get(value2).repoTimes>=k){
                    cnt += 1;
                }
            }
            preAns.add(cnt);
        }

        int[] answer = {preAns.size()};
        for(int i = 0 ; i<preAns.size(); i++){
            answer[i] = preAns.get(i);
        }
        return answer;
    }
    static class myObject{              // value값에 해당하는 객체 생성
        int repoTimes = 0;
        ArrayList<String> reporter = new ArrayList<>();
    }
}