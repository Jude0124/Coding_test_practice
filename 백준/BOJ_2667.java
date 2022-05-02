import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class BOJ_2667 {
    static int [][] table;
    static int size;
    static Queue<int []> queue = new LinkedList<>();
    static int area;
    
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        String cnt = sc.next();
        size = Integer.valueOf(cnt);
        table = new int [size+2][size+2];
        for(int garo = 1 ; garo < size+1; garo++){
            String temp = sc.next();
            for (int sero = 1 ; sero < size+1 ; sero++){
                table[garo][sero]= temp.charAt(sero-1)-'0';
            }
        }
        sc.close();
        ArrayList <Integer> answer = getAnswer();
        for(int ans : answer){
            System.out.println(ans);
        }
    }

    static ArrayList<Integer> getAnswer(){
        ArrayList<Integer> answer = new ArrayList<>();
        int cnt = 0;
        answer.add(cnt,0);

        for(int i = 1 ; i<size+1; i++){
            for(int j = 1 ; j<size+1; j++){
                if (table[i][j]== 1){
                    area=0;
                    cnt++;
                    queue.add(new int [] {i,j});
                    answer.add(cnt,getArea());
                }
            }
        }
        return answer;
    }
    static int getArea(){
        while(!queue.isEmpty()){
            int [] t = queue.poll();
            area++;
            table[t[0]][t[1]] = 0;
            if(table[t[0]][t[1]-1] == 1){
                queue.add(new int [] {t[0],t[1]-1});
            };
            if(table[t[0]][t[1]+1] == 1){
                queue.add(new int [] {t[0],t[1]+1});
            };
            if(table[t[0]-1][t[1]] == 1){
                queue.add(new int [] {t[0]-1,t[1]});
            };
            if(table[t[0]+1][t[1]] == 1){
                queue.add(new int [] {t[0]+1,t[1]});
            };
            

        }
        return area;
    }

}