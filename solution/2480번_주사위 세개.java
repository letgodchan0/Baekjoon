import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        Collection<Integer> list = new ArrayList<>();
        list.add(a); list.add(b); list.add(c);

        if (a == b && b == c){
            System.out.println(10000+(a*1000));
        }else if (a != b && b != c && a != c){
            System.out.println(Collections.max(list) * 100);
        } else if (a == b && a != c){
            System.out.println(1000 + (a*100));
        } else if (b==c && b != a){
            System.out.println(1000 + (b*100));
        } else if (a == c && c != b){
            System.out.println(1000 + (c*100));
        }
    }
}