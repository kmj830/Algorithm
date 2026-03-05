import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        br.readLine();


        HashSet<Integer> a = Arrays.stream(br.readLine().split(" ")).map(Integer::valueOf).collect(Collectors.toCollection(HashSet::new));
        HashSet<Integer> b = Arrays.stream(br.readLine().split(" ")).map(Integer::valueOf).collect(Collectors.toCollection(HashSet::new));

        HashSet<Integer> temp = (HashSet<Integer>) a.clone();

        a.retainAll(b);

        temp.addAll(b);
        temp.removeAll(a);

        System.out.println(temp.size());
    }
}