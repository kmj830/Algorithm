import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        int n = Integer.parseInt(input); //분해합

        int m = 0; //생성자

        for (int i = 0; i < n; i++) {
            int total = i;
            int temp = i;

            while (temp > 10) {
                total += temp % 10;
                temp /= 10;
            }
            total += temp;
            if (total == n) {
                m = i;
                break;
            }
        }

        System.out.println(m);
    }
}