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
        StringBuilder sb = new StringBuilder();

        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int n = arr[0];
        int k = arr[1];


        ArrayDeque<Integer> deque = new ArrayDeque<>();
        ArrayList<Integer> result = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            deque.addLast(i);
        }

        while (deque.size() != 0) {
            for (int i = 0; i < k-1; i++) {
                deque.addLast(deque.pollFirst());
            }
            result.add(deque.pollFirst());
        }
        String temp = result.stream()
                .map(String::valueOf)
                .collect(Collectors.joining(", "));
        sb.append("<");
        sb.append(temp);
        sb.append(">");
        System.out.println(sb);

    }
}