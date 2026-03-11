import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        ArrayDeque<Integer> deque = new ArrayDeque<>();
        ArrayDeque<Integer> line = new ArrayDeque<>();
        while (st.hasMoreTokens()) {
            deque.add(Integer.parseInt(st.nextToken()));
        }
        int num = 1;
        for (int i = 0; i < n; i++) {
            Integer now = deque.pollFirst();
            if (now == num) {
                num++;
                while (true) {
                    Integer lineFirst = line.peekFirst();
                    if (lineFirst != null && lineFirst == num) {
                        num++;
                        line.pollFirst();
                    }else {
                        break;
                    }
                }
            } else {
                line.addFirst(now);
            }
        }
        boolean flag = true;


        while (!line.isEmpty()) {
            Integer now = line.pollFirst();
            if (now == num) {
                num++;
            }else {
                flag = false;
                break;
            }
        }
        System.out.println(flag ? "Nice" : "Sad");
    }
}