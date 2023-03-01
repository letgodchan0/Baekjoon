import java.io.*;
import java.sql.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        HashMap<Integer, Integer> number = new HashMap();

        for (int i = 1; i <31; i++){
            number.put(i, 0);
        }

        for (int i = 0; i < 28; i++){
            int n = Integer.parseInt(br.readLine());
            number.put(n, 1);
        }

        List<Integer> lst = new ArrayList();

        for (int i = 1; i <31; i++){
            if (number.get(i) == 0){
                lst.add(i);
            }
        }

        int max = lst.get(0);
        int min = lst.get(0);

        for (int n: lst
             ) {
            if (n > max){
                max = n;
            }

            if (n < min){
                min = n;
            }
        }
        System.out.println(min);
        System.out.println(max);
    }
}