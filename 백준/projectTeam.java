import java.util.*;

public class projectTeam {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        ArrayList<Integer> member = new ArrayList<>();
        ArrayList<Integer> team = new ArrayList<>();
        for (int i = 0; i < num * 2; i++) {
            member.add(sc.nextInt());
        }
        Collections.sort(member);
        for (int i = 0; i < num; i++) {
            team.add(member.get(i) + member.get(num * 2 - 1 - i));
        }

        System.out.println(Collections.min(team));
    }
}