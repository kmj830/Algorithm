import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int count = 0;
        int gap = 2;
        for (int i = 1; i < n + 1; ) {
            i += 1 + gap;
            count++;
            gap += 2;
        }
        System.out.println(count);
    }
}