import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            int[] array = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            switch (array[0]) {
                case 1:
                    stack.addLast(array[1]);
                    break;
                case 2:
                    if (stack.isEmpty()) {
                        sb.append(-1).append("\n");
                    }else {
                        sb.append(stack.pollLast()).append("\n");
                    }
                    break;
                case 3:
                    sb.append(stack.size()).append("\n");
                    break;
                case 4:
                    if (stack.isEmpty()) {
                        sb.append(1).append("\n");
                    } else {
                        sb.append(0).append("\n");
                    }
                    break;
                case 5:
                    if (stack.isEmpty()) {
                        sb.append(-1).append("\n");
                    }else {
                        sb.append(stack.getLast()).append("\n");
                    }
                    break;
                default:
                    throw new IllegalStateException("Unexpected value: " + array[0]);
            }
        }
        System.out.println(sb);
    }
}