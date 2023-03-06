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
            basket.add(0);
        }

        for (int a=0; a<M; a++){
            StringTokenizer stt = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(stt.nextToken());
            int j = Integer.parseInt(stt.nextToken());
            int k = Integer.parseInt(stt.nextToken());

            for (int check = i; check < j+1; check++ ){
                basket.set(check, k);
            }
        }

        for (int i=1; i < N; i++){
            System.out.print(basket.get(i) + " ");
        }
        System.out.println(basket.get(N));
    }
}