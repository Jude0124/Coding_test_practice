import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class BOJ_2667 {
    static int [][] table;                                  // 빈 좌표공간 만들어주기
    
    static int size;                                        //size = 공간의 가로 세로 길이 => size * size

    static Queue<int []> queue = new LinkedList<>();        //들어갔다가 나오는 빈 큐(컨베이어 벨트) 만들어주기

    static int area;                                        //각각의 영역의 넓이를 구했을 때마다 해당 값을 저장해줄 변수

    static int cnt;                                         //
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


            if(table[t[0]][t[1]-1] == 1){   /// 위로 한칸탐색
                queue.add(new int [] {t[0],t[1]-1});
                table[t[0]][t[1]-1] = 0;
            };

            if(table[t[0]][t[1]+1] == 1){  /// 아래로 한칸탐색
                queue.add(new int [] {t[0],t[1]+1});
                table[t[0]][t[1]+1] = 0;
            };

            if(table[t[0]-1][t[1]] == 1){       //왼쪽으로 한칸탐색
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