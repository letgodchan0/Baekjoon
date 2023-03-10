import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        List<Integer> list = new ArrayList();
        while (st.hasMoreTokens()){
            list.add(Integer.parseInt(st.nextToken()));
        }
        List<Integer> check = Arrays.asList(1, 1, 2, 2, 2, 8);

        for (int i = 0; i < 6; i++){
            System.out.print(check.get(i) - list.get(i)+" ");
        }
    }
}