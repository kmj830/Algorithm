import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int n = temp[0];
        int m = temp[1];

        HashSet<String> strList = new HashSet<>();

        for (int i = 0; i < n; i++) {
            strList.add(br.readLine());
        }

        int count = 0;

        for (int i = 0; i < m; i++) {
            String input = br.readLine();
            if (strList.contains(input)) {
                count++;
            }
        }
        System.out.println(count);
    }
}