import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int total = Integer.parseInt(br.readLine());
        int N = Integer.parseInt((br.readLine()));
        int check = 0;
        for (int i = 0; i < N; i++){
            String info = br.readLine();;
            StringTokenizer st = new StringTokenizer(info);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            check += (a*b);
        }

        if (check == total){
            System.out.println("Yes");
        } else{
            System.out.println("No");
        }
    }
}