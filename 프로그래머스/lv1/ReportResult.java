import java.util.*;

public class ReportResult {
    public int[] solution(String[] id_list, String[] report, int k) {
        Map<String, myObject> reportLog = new HashMap<>();
        ArrayList<Integer> preAns = new ArrayList<>();
        HashSet<String> report2 = new HashSet<>(Arrays.asList(report));
        String[] repoLast = report2.toArray(new String[0]);
        for (String key : id_list){
            reportLog.put(key, new myObject());
        }

        for (String repo : repoLast){
            String[] temp = repo.split(" ");
            reportLog.get(temp[0]).repoTimes++;
            reportLog.get(temp[0]).reporter.add(temp[1]);

        }

        for(String key : id_list){
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
    static class myObject{
        int repoTimes = 0;
        ArrayList<String> reporter = new ArrayList<>();
    }
}