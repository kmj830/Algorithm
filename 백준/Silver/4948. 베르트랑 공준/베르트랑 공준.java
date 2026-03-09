import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int[] arr = new int[123456*2+1];
        for (int i = 2; i <= 123456*2; i++) {
            arr[i] = i;
        }

        for (int i = 2; i <= 123456*2; i++) {
            if (arr[i]==0) continue;
            for (int j = 2 * i; j <= 123456*2; j += i) {
                arr[j] = 0;
            }
        }
        while (true) {
            int n = Integer.parseInt(br.readLine());
            if (n == 0) {
                break;
            }
            int count = 0;

            for (int i = n+1; i <= n * 2; i++) {
                if (arr[i] != 0) {
                    count++;
                }
            }
            sb.append(count).append("\n");
        }
        System.out.println(sb);
    }
}