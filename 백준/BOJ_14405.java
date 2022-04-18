import java.util.Scanner;

public class BOJ_14405 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String pkc = sc.nextLine();
        sc.close();

        while(pkc.length()>2){
            if(pkc.substring(0,3).equals("chu")){
                pkc = pkc.substring(3);
            }else if(pkc.substring(0,2).equals("pi") || pkc.substring(0,2).equals("ka")){
                pkc = pkc.substring(2);
            }else{
                break;
            }
        }
        if (pkc.equals("") || pkc.equals("pi") || pkc.equals("ka")){
            System.out.println("YES");
        }else{
            System.out.println("NO");
        }
    }
}
