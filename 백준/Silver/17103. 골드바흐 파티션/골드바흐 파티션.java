import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int[] arr = new int[1000000+1];
        for (int i = 2; i <= 1000000; i++) {
            arr[i] = i;
        }

        for (int i = 2; i <= 1000000; i++) {
            if (arr[i]==0) continue;
            for (int j = 2 * i; j <= 1000000; j += i) {
                arr[j] = 0;
            }
        }

        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            int count = 0;
            for (int j = 2; j <= n / 2; j++) {
                if (arr[j] != 0 && arr[n - j] != 0) {
                    count++;
                }
            }
            sb.append(count).append("\n");
        }
        System.out.println(sb);

    }
}