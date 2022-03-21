import java.util.*;

public class Tresure_BOJ_1026{
    public static void main(String[] args) {
        int answer = 0;
        Scanner sc = new Scanner(System.in);
        int len = sc.nextInt();
        ArrayList<Integer> T1 = new ArrayList<>();
        ArrayList<Integer> T2 = new ArrayList<>();
        for (int i = 0; i < len; i++) {
            T1.add(sc.nextInt());
        }

        for (int i = 0; i < len; i++) {
            T2.add(sc.nextInt());
        }

        Collections.sort(T1);
        Collections.sort(T2);

        for (int i = 0; i < len; i++) {
            answer += T1.get(i)*T2.get(len-1-i);
        }

        System.out.println(answer);
    }
}