import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int count = 0;
        int i = 665;

        while (true) {
            i += 1;
            int temp = i;
            int straightCount = 0;
            while (true) {
                int r = temp % 10;
                if (r == 6) {
                    straightCount += 1;
                } else straightCount = 0;
                if (straightCount == 3) {
                    count += 1;
                    break;
                }
                if (temp < 10) {
                    break;
                }
                temp /= 10;
            }
            if (count == n) {
                System.out.println(i);
                break;
            }
        }
    }
}