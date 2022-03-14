import java.util.ArrayList;

//  브루트 포스로 풀어보자

public class takingGroupPhoto {
    public static void main(String[] args) {
        solution(2,new String [] {"N~F=0", "R~T>2"});
        // solution(2,new String [] {"M~C<2", "C~M>1"});
    }

    public static int solution(int n, String[] data) {
        int answer = 0;
        String friends = "ACFJMNRT";
        permutation(friends,0,friends.length());
        return answer;
    }

    static void permutation(String friends, int depth, int len){
        if(depth == friends.length()){
        System.out.println(friends);
        return;
        }
        for(int i=depth; i <len; i++) {
            swap(friends, depth, i);
            permutation(friends, depth+1, len);
            swap(friends, depth, i);
        }

    }
    
    static void swap(String friends, int depth, int i)
    {
        char[] ch = friends.toCharArray();
        char temp = ch[depth];
        ch[depth] = ch[i];
        ch[i] = temp;
        friends = String.valueOf(ch);
        // System.out.println(friends);
    }
}
