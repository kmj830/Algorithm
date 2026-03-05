import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());

        int[] array = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < n; i++) {
            if (map.containsKey(array[i])) {
                map.replace(array[i], map.get(array[i]) + 1);
            }else {
                map.put(array[i], 1);
            }
        }
        int m = Integer.parseInt(br.readLine());
        int[] arrayM = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        for (int i : arrayM) {
            if (map.containsKey(i)) {
                sb.append(map.get(i)).append(" ");
            }else {
                sb.append(0).append(" ");
            }
        }
        System.out.println(sb);
    }
}