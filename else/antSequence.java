import java.util.Scanner;

public class antSequence {
    public static void main(String[] args) {
        ant();
    }

    static String ant() {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        sc.close();
        int now = 1;
        String ant = "1";        
        while(num != now){
            ant = calc(ant);
            now++;
        }
        System.out.println(ant);
        
        return ant;

    }

    static String calc(String before){
        char pre = before.charAt(0);
        int cnt = 1;
        String next = "";
        for (int i = 1 ; i< before.length() ;i++){
            if (pre == before.charAt(i)){
                cnt++;
            }else{
                next += pre+""+cnt;
                pre = before.charAt(i);
                cnt = 1;
            }
        }
        next += pre+""+cnt;
        return next;
    }
}