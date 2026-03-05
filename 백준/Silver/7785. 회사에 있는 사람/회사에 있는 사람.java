import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        HashSet<String> log = new HashSet<>();
        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().split(" ");
            if (s[1].equals("enter")) {
                log.add(s[0]);
            }else {
                log.remove(s[0]);
            }
        }
        ArrayList<String> strings = new ArrayList<>(log);
        strings.sort(Comparator.reverseOrder());
        for (String string : strings) {
            System.out.println(string);
        }
    }
}