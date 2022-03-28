import java.util.Scanner;

public class BOJ_15650 {
    static boolean[] visited;
    static int Pick;
    static int Entire;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Entire = sc.nextInt()+1;
        Pick = sc.nextInt();
        visited = new boolean[Entire];

        back(1, 0);

        sc.close();
    }

    static void back(int start, int depth) {
        if (depth == Pick) {
            print(visited);
            return;
        }

        for (int i = start; i < Entire; i++) {
            visited[i] = true;
            back(i + 1, depth + 1);
            visited[i] = false;

        }
    }

    static void print(boolean[] visited){
        for (int i = 1 ; i< Entire ; i++){
            if(visited[i]){
                System.out.print(i + " ");
            }
        }
        System.out.println();
    }

}
