import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        //BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String number = br.readLine();

        String[] check = number.split(" ");

        int a = Integer.parseInt(check[0]);
        int b = Integer.parseInt(check[1]);
        int c = Integer.parseInt(check[2]);

        System.out.println((a+b)%c);
        System.out.println(((a%c)+(b%c))%c);
        System.out.println((a*b)%c);
        System.out.println(((a%c)*(b%c))%c);


    }
}