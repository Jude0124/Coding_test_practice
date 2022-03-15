import java.util.LinkedList;
class Solution
{
    final int[][] movement = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
    public int solution(int[][] maps) {
        LinkedList<Integer> queue = new LinkedList<Integer>();
        LinkedList<Integer> route = new LinkedList<Integer>();
        int mrow = maps.length, mcol = maps[0].length;
        boolean[][] visited = new boolean[mrow][mcol];
        queue.add(0);
        route.add(1);
        visited[0][0] = true;
        while(!queue.isEmpty())
        {
            int code = queue.remove(), nowRoute = route.remove();
            int row = code / mcol, col = code % mcol;
            for(int i=0; i<movement.length; ++i)
            {
                int nrow = row + movement[i][0], ncol = col + movement[i][1];
                if(nrow == mrow-1 && ncol == mcol-1)
                    return ++nowRoute;
                if(nrow >= 0 && nrow < mrow && ncol >= 0 && ncol < mcol && maps[nrow][ncol] == 1 && !visited[nrow][ncol])
                {
                    queue.add(nrow * mcol + ncol);
                    route.add(nowRoute+1);
                    visited[nrow][ncol] = true;
                }
            }
        }
        return -1;
    }
}
