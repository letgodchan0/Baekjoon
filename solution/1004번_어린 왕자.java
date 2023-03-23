import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static boolean[][] isInside;
    static int[] dx = { 1, -1, 0, 0 };
    static int[] dy = { 0, 0, 1, -1 };

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int startX = Integer.parseInt(st.nextToken());
            int startY = Integer.parseInt(st.nextToken());
            int endX = Integer.parseInt(st.nextToken());
            int endY = Integer.parseInt(st.nextToken());
            int N = Integer.parseInt(br.readLine());

            isInside = new boolean[2][N];

            for (int j = 0; j < N; j++) {
                st = new StringTokenizer(br.readLine());
                int centerX = Integer.parseInt(st.nextToken());
                int centerY = Integer.parseInt(st.nextToken());
                int radius = Integer.parseInt(st.nextToken());

                if (isPointInside(startX, startY, centerX, centerY, radius)) {
                    isInside[0][j] = true;
                }
                if (isPointInside(endX, endY, centerX, centerY, radius)) {
                    isInside[1][j] = true;
                }
            }

            int answer = 0;
            for (int j = 0; j < N; j++) {
                if (isInside[0][j] != isInside[1][j]) {
                    answer++;
                }
            }

            System.out.println(answer);
        }
    }

    static boolean isPointInside(int x, int y, int cx, int cy, int r) {
        return Math.pow(x - cx, 2) + Math.pow(y - cy, 2) < Math.pow(r, 2);
    }
}