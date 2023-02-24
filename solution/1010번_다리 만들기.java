import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[][] memo = new int[30][30];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            sb.append(combination(Math.max(a, b), Math.min(a, b)) + "\n");
        }
        System.out.print(sb);
    }

    static int combination(int n, int r) {
        if (r == 0 || n == r) return 1;

        if (memo[n][r] != 0) return memo[n][r];
        return memo[n][r] = combination(n-1, r-1) + combination(n-1, r);
    }
}