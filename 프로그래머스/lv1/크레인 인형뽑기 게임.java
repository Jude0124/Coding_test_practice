import java.util.Stack;

class DollDrawingMachine {
    
    public int dollDrawingMachine(int[][] board, int[] moves) {
     
        int cnt = 0;
        Stack<Integer> stack = new Stack<Integer>();
        for(int i : moves) {
            for(int j = 0; j < board.length; j++) { // column의 깊이만큼
                if(board[j][i-1] != 0) { // 인형을 만났을 때
                    if(!stack.isEmpty()&&stack.peek() == board[j][i-1]) {
                        stack.pop();
                        cnt+=2;
                    } else {
                        stack.push(board[j][i-1]);
                    }
                    board[j][i-1] = 0; // map에서 꺼낸 인형 삭제
                    break;
                }
            }
        }

        return cnt;
    }

}