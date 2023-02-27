import java.io.*;
import java.sql.SQLOutput;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt((br.readLine()));
        int count = N / 4;
        String s = "";

        for (int i = 0; i < count; i++){
            s += "long ";
        }

        System.out.println(s + "int");

    }
}