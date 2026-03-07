import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.concurrent.ForkJoinPool;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String temp = br.readLine();
        HashSet<String> set = new HashSet<>();
        for (int i = 0; i < temp.length(); i++) {
            for (int j = i+1; j < temp.length()+1; j++) {
                set.add(temp.substring(i, j));
            }
        }
        System.out.println(set.size());

    }
}