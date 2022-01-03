import java.util.Scanner;

class CountingBoxStar {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(), b = sc.nextInt();   
        String star = "";
        
        for(int i = 0 ; i < a ; i++){
            star += "*";    
        }
        for(int j = 0 ; j < b ; j++){
            System.out.println(star);
        }
        sc.close();
    }
}