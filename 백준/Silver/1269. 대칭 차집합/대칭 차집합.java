import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        br.readLine();
        int count = 0;
        HashSet<Integer> a = Arrays.stream(br.readLine().split(" ")).map(Integer::valueOf).collect(Collectors.toCollection(HashSet::new));
        HashSet<Integer> b = Arrays.stream(br.readLine().split(" ")).map(Integer::valueOf).collect(Collectors.toCollection(HashSet::new));

        for (int i : a) {
            if (b.contains(i)) {
                count++;
            }
        }
        System.out.println(a.size() + b.size() - 2 * count);
    }
}