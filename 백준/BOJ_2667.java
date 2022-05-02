import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class BOJ_2667 {
    static int [][] table;
    static int size;
    static Queue<int []> queue = new LinkedList<>();
    static int area;
    static int cnt;
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        String num = sc.next();
        size = Integer.valueOf(num);
        table = new int [size+2][size+2];
        for(int garo = 1 ; garo < size+1; garo++){
            String temp = sc.next();
            for (int sero = 1 ; sero < size+1 ; sero++){
                table[garo][sero]= temp.charAt(sero-1)-'0';
            }
        }
        sc.close();
        ArrayList <Integer> answer = getAnswer();
        System.out.println(cnt);
        Collections.sort(answer);
        for(int ans : answer){
            System.out.println(ans);
        }
    }

    static ArrayList<Integer> getAnswer(){
        ArrayList<Integer> answer = new ArrayList<>();
        cnt = 0;

        for(int i = 1 ; i<size+1; i++){
            for(int j = 1 ; j<size+1; j++){
                if (table[i][j]== 1){
                    area=0;
                    cnt++;
                    queue.add(new int [] {i,j});
                    table[i][j] = 0;
                    answer.add(cnt-1,getArea());
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
                table[t[0]][t[1]-1] = 0;
            };
            if(table[t[0]][t[1]+1] == 1){
                queue.add(new int [] {t[0],t[1]+1});
                table[t[0]][t[1]+1] = 0;
            };
            if(table[t[0]-1][t[1]] == 1){
                queue.add(new int [] {t[0]-1,t[1]});
                table[t[0]-1][t[1]] = 0;
            };
            if(table[t[0]+1][t[1]] == 1){
                queue.add(new int [] {t[0]+1,t[1]});
                table[t[0]+1][t[1]] = 0;
            };
            

        }
        return area;
    }

}