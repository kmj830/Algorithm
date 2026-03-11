import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            ArrayDeque<String> arr = new ArrayDeque<>(List.of(br.readLine().split("")));
            ArrayDeque<String> waiting = new ArrayDeque<>();
            while (!arr.isEmpty()) {
                String s = arr.pollLast();
                waiting.addFirst(s);
                while (true) {
                    String s1 = waiting.pollFirst();
                    if (s1==null) {
                        break;
                    }
                    String s2 = waiting.pollFirst();
                    if (s2 == null) {
                        waiting.addFirst(s1);
                        break;
                    }
                    if (!s1.equals("(") || !s2.equals(")")) {
                        waiting.addFirst(s1);
                        waiting.addFirst(s2);
                        break;
                    }
                }
            }
            if (waiting.isEmpty()) {
                sb.append("YES");
            } else sb.append("NO");
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
