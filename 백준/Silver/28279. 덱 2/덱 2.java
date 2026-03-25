import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        ArrayDeque<Integer> deque = new ArrayDeque<>();

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            switch (cmd) {
                case "1":
                    int addFirst = Integer.parseInt(st.nextToken());
                    deque.addFirst(addFirst);
                    break;
                case "2":
                    int addLast = Integer.parseInt(st.nextToken());
                    deque.addLast(addLast);
                    break;
                case "3":
                    if (deque.isEmpty()) {
                        sb.append(-1).append("\n");
                    }else {
                        sb.append(deque.pollFirst()).append("\n");
                    }
                    break;
                case "4":
                    if (deque.isEmpty()) {
                        sb.append(-1).append("\n");
                    }else {
                        sb.append(deque.pollLast()).append("\n");
                    }
                    break;
                case "5":
                    sb.append(deque.size()).append("\n");
                    break;
                case "6":
                    sb.append(deque.isEmpty() ? 1 : 0).append("\n");
                    break;
                case "7":
                    if (deque.isEmpty()) {
                        sb.append(-1).append("\n");
                    }else {
                        sb.append(deque.peekFirst()).append("\n");
                    }
                    break;
                case "8":
                    if (deque.isEmpty()) {
                        sb.append(-1).append("\n");
                    }else {
                        sb.append(deque.peekLast()).append("\n");
                    }
                    break;
            }
        }
        System.out.println(sb);
    }
}