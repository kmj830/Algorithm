import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            long m = Long.parseLong(br.readLine());
            while (!isPrime(m)) {
                m++;
            }
            sb.append(m).append("\n");
        }
        System.out.println(sb);

    }

    private static boolean isPrime(long n) {
        if (n < 2) {
            return false;
        }
        for (long i = 2; i*i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}