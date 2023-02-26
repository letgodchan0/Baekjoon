import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.parseInt(br.readLine());
        String b = br.readLine();
        int n = b.length();
        int c = Integer.parseInt(b);
        // reverse
        List<Character> list = new ArrayList<>();

        for (char each : b.toCharArray()){
            list.add(each);
        }
        Collections.reverse(list);

        for (int i = 0; i < n; i++){
            int val = Character.getNumericValue(list.get(i));
            System.out.println(val * a);
        }
        System.out.println(a*c);

    }
}