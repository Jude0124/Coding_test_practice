import java.util.*;

public class BOJ_1026{
    public static void main(String[] args) {
        int answer = 0;
        Scanner sc = new Scanner(System.in);
        int len = sc.nextInt();
        ArrayList<Integer> people = new ArrayList<>();
        for (int i = 0; i < len; i++) {
            people.add(sc.nextInt());
        }
        Collections.sort(people);

        for (int i = 0; i < len; i++) {
            answer += people.get(i)*(len-i);
        }

        System.out.println(answer);
    }
}