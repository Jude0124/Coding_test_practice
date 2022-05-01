import java.util.Scanner;
import java.util.Arrays;

public class BOJ_1213 {
    static char arr[];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String pelindrom = sc.nextLine();
        pelindrom += "[";
        int len = pelindrom.length();
        sc.close();

        for (int i = 0; i < len; i++) {
            pelindrom.charAt(i);
            arr = pelindrom.toCharArray();
            Arrays.sort(arr);
        }
        
        makeIt(arr);

    }

    static void makeIt(char arr[]) {
        boolean odd = false;
        
        String center = "";
        String answer1 = "";
        String answer2 = answer1;

        int cnt = 0;
        char before = arr[0];
        char now;
        for (int i = 1; i < arr.length; i++) {
            now = arr[i];
            if (now == before) {
                cnt++;
                if (cnt % 2 == 1) {
                    answer1 = answer1 +  before;
                    answer2 = before + answer2;
                }
            } else {
                if (cnt % 2 == 0) {
                    if (odd == false) {
                        odd = true;
                        center += before;
                    } else {
                        System.out.println("I'm Sorry Hansoo");
                        return;
                    }
                } 
                cnt = 0;
                before = now;
            }
        }

        System.out.println(answer1 + center + answer2);
    }
}