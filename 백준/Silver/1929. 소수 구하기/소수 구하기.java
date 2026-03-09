import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int[] inputArr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int m = inputArr[0], n = inputArr[1];
        int[] arr = new int[n+1];
        for (int i = 2; i <= n; i++) {
            arr[i] = i;
        }

        for (int i = 2; i <= n; i++) {
            if (arr[i]==0) continue;
            for (int j = 2 * i; j <= n; j += i) {
                arr[j] = 0;
            }
        }

        for (int i = m; i <= n; i++) {
            if (arr[i] != 0) {
                sb.append(i).append("\n");
            }
        }
        System.out.println(sb);
    }
}