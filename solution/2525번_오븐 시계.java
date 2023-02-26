import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] current = br.readLine().split(" ");
        int time = Integer.parseInt(br.readLine());
        int hour = Integer.parseInt(current[0]); int minutes = Integer.parseInt(current[1]);

        int check = hour * 60 + minutes + time;

        if (check > 1439){
            check -= 1440;
        }
        int div = check / 60;
        int mod = check - (60 * div);

        System.out.print(div);
        System.out.print(" ");
        System.out.print(mod);
    }
}