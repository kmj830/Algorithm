import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] a = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] b = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        long lcm = lcm(a[1], b[1]);
        long i = lcm / a[1] * a[0] + lcm / b[1] * b[0];
        long gcd = gcd(i, lcm);
        System.out.println(i/gcd + " " + lcm/gcd);

    }

    private static long lcm(long a, long b) {
        return a * b / (gcd(a, b));
    }

    private static long gcd(long a, long b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }
}