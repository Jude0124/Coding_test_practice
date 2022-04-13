import java.util.ArrayList;
import java.util.Scanner;

public class BOJ_9461 {
    static ArrayList<Integer> arr;
    static ArrayList<Integer> answer;
    public static void main(String[] args) {
        arr = new ArrayList<>();
        arr.add(0,1);
        arr.add(1,1);
        arr.add(2,1);
        arr.add(3,2);
        arr.add(4,2);

        int i = 5;
        while (i<101){
            arr.add(i,arr.get(i-1)+arr.get(i-5));
            i++;
        }
        System.out.println(arr.toString());

        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();

        for(int j = 0 ; j < num ; j++){
            answer.add(j,arr.get(sc.nextInt()-1));
        }
        sc.close();
        for (int ans : answer){
            System.out.println(ans);
        }
    }
}