import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int last = Integer.parseInt(br.readLine());
        int first = last;
        int gap = 0;
        for (int i = 1; i < n; i++) {
            int temp = Integer.parseInt(br.readLine());
            int gapTemp = temp - last;
            last = temp;
            if (i > 1) {
                gap = gcd(gapTemp, gap);
            } else gap = gapTemp;
        }

        System.out.println((last - first) / gap + 1 - n);
    }

    private static int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }
}