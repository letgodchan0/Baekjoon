import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String numbers = br.readLine();
        StringTokenizer st = new StringTokenizer(numbers);
        int check = Integer.parseInt(br.readLine());
        int answer = 0;

        for (int i = 0; i < N; i++){
            if(check == Integer.parseInt(st.nextToken())){
                answer += 1;
            }
        }
        System.out.println(answer);
    }
}