import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        List<Integer> basket = new ArrayList();

        for (int i=0; i<N+1; i++){
            basket.add(i);
        }

        for (int a=0; a<M; a++){
            StringTokenizer stt = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(stt.nextToken());
            int j = Integer.parseInt(stt.nextToken());

            int bef = basket.get(i);
            int aft = basket.get(j);

            basket.set(i, aft);
            basket.set(j, bef);
        }

        for (int i=1; i < N; i++){
            System.out.print(basket.get(i) + " ");
        }
        System.out.println(basket.get(N));
    }
}