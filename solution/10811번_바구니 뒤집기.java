import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        List<Integer> basket = new ArrayList();

        for (int i=0; i<N; i++){
            basket.add(i+1);
        }

        for (int a=0; a<M; a++){
            StringTokenizer stt = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(stt.nextToken());
            int j = Integer.parseInt(stt.nextToken());

            Collections.reverse(basket.subList(i-1, j));

        }

        for (int i=0; i < N-1; i++){
            System.out.print(basket.get(i) + " ");
        }
        System.out.println(basket.get(N-1));
    }
}