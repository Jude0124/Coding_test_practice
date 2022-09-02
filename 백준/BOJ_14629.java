import java.util.ArrayList;
import java.util.Scanner;

public class BOJ_14629 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Long number = sc.nextLong();
        
        ArrayList<Integer> num = new ArrayList<>();
        for (int i = 0 ; i < 10 ; i++){
            num.add(i);
        }

        if (number >= 9876543210L){
            System.out.println("9876543210");
        } else{
            String numberstr = String.valueOf(number);
            int cnt = numberstr.length()-1;
            long temp = 0L;
            while (cnt !=-1){
                long min = 0L;
                for(int n : num){
                    if (min>abs(number-Math.pow(10,cnt)*n+temp))
                    min = abs(number-Math.pow(10,cnt)*n+temp);
                }
                
            }
            
        }
    }   
    
}
