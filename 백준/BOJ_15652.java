import java.util.Scanner;
 
public class BOJ_15652 {
 
	public static int n;
    public static int m;
	public static int[] arr;
 
	public static void main(String[] args) {
 
		Scanner in = new Scanner(System.in);
 
		n = in.nextInt();
		m = in.nextInt();
		arr = new int[M];
 
		dfs(1, 0);
 
	}
 
	public static void dfs(int where, int depth) {
 
		if (depth == m) {
			for (int val : arr) {
				System.out.print(val + " ");
			}
			System.out.println();
			return;
		}
 
		for (int i = where; i <= n; i++) {
			arr[depth] = i;
			dfs(i, depth + 1);
		}
 
	}
 
}