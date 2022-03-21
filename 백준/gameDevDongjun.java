import java.util.*;

public class gameDevDongjun {
    public static void main(String[] args) {
        int answer = 0;
        Scanner sc = new Scanner(System.in);
        int len = sc.nextInt();
        ArrayList<Integer> levels = new ArrayList<>();
        for (int i = 0; i < len; i++) {
            levels.add(sc.nextInt());
        }
        
        int pre = levels.get(len-1)+1;
        for (int i = 0; i < len; i++) {
            int now =levels.get(len-1-i);
            if (pre <= now){
                answer += now-pre+1;
                pre = pre-1;
                        
            }else{
                pre = now;
            }
        }
        System.out.println(answer);

    }
}
