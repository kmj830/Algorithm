import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        ArrayDeque<Pair> deque = new ArrayDeque<>();
        ArrayList<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            deque.addLast(new Pair(i + 1, arr[i]));
        }
        while (!deque.isEmpty()) {
            Pair pair = deque.pollFirst();
            if (pair.y > 0 && !deque.isEmpty()) {
                for (int i = 0; i < pair.y-1; i++) {
                    deque.addLast(deque.pollFirst());
                }
            } else if (pair.y < 0 && !deque.isEmpty()) {
                for (int i = 0; i < Math.abs(pair.y); i++) {
                    deque.addFirst(deque.pollLast());
                }
            }
            result.add(pair.x);
        }
        System.out.println(result.stream().map(String::valueOf).collect(Collectors.joining(" ")));
    }

    static class Pair {
        int x, y;

        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}