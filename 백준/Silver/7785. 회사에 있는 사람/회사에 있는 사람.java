import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        HashSet<String> log = new HashSet<>();
        for (int i = 0; i < n; i++) {
            String s = br.readLine().split(" ")[0];
            if (!log.add(s)) {
                log.remove(s);
            }
        }
        ArrayList<String> strings = new ArrayList<>(log);
        strings.sort(Comparator.reverseOrder());
        for (String string : strings) {
            sb.append(string).append("\n");
        }
        System.out.println(sb);
    }
}