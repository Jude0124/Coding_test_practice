import java.util.Scanner;

public class BOJ_5585 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int answer = 0;
        int money = 1000-sc.nextInt();

        answer  += money/500;
        money %= 500;
        
        answer += money/100;
        money %= 100;

        answer += money/50;
        money %= 50;

        answer += money/10;
        money %= 10;


        answer += money/5;
        money %= 5;

        answer += money/1;
        money %= 1;

        System.out.println(answer);
    }
}
