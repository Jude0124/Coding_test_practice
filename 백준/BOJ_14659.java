import java.util.*;

public class BOJ_14659{
    public static void main(String[] args) {
        int answer = 0;
        Scanner sc = new Scanner(System.in);
        int len = sc.nextInt();
        ArrayList<Integer> mountains = new ArrayList<>();
        for (int i = 0; i < len; i++) {
            mountains.add(sc.nextInt());
        }
        int pre = mountains.get(0);
        int cntnow = 0;
        for (int i = 1; i < len; i++) {
            int now =mountains.get(i);
            if (pre < now){
                pre = now;
                if (answer<cntnow){
                    answer = cntnow;
                }
                cntnow = 0;
            }else{
                cntnow++;
            }
        }
        if(answer<cntnow){
            answer = cntnow;
        }
        System.out.println(answer);

    }
}
