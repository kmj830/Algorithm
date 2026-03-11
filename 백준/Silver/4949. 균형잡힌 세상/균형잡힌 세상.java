import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {
            String temp = br.readLine();
            if (temp.equals(".")) break;

            String[] split = temp.split("");
            ArrayDeque<String> deque = new ArrayDeque<>();
            ArrayDeque<String> waiting = new ArrayDeque<>();
            for (String s : split) {
                switch (s) {
                    case "(":
                        deque.addLast("(");
                        break;
                    case ")":
                        deque.addLast(")");
                        break;
                    case "[":
                        deque.addLast("[");
                        break;
                    case "]":
                        deque.addLast("]");
                        break;
                }
            }

            while (!deque.isEmpty()) {
//                br.readLine();
//                System.out.println("deque Before= " + deque);
//                System.out.println("waiting Before= " + waiting);
                String s = deque.pollLast();
                waiting.addFirst(s);
//                System.out.println("deque = " + deque);
//                System.out.println("waiting = " + waiting);
//                System.out.println("s = " + s);
                while (true) {
                    String s1 = waiting.pollFirst();
                    if (s1 == null) {
                        break;
                    }
                    String s2 = waiting.pollFirst();
                    if (s2 == null) {
                        waiting.addFirst(s1);
                        break;
                    }
                    if (s1.equals("(") && s2.equals(")")) {
//                        System.out.println("DELETE (,)");
                    } else if (s1.equals("[") && s2.equals("]")) {
//                        System.out.println("DELETE [,]");
                    }else {
                        waiting.addFirst(s2);
                        waiting.addFirst(s1);
                        break;
                    }
//                    System.out.println("waiting After= " + waiting);

                }
            }
            if (waiting.isEmpty()) {
                sb.append("yes");
            } else sb.append("no");
            sb.append("\n");
        }
        System.out.println(sb);
    }
}