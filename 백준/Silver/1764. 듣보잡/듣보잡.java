import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());

        HashSet<String> setN = new HashSet<>();
        for (int i = 0; i < n; i++) {
            setN.add(br.readLine());
        }

        HashSet<String> setM = new HashSet<>();
        for (int i = 0; i < m; i++) {
            setM.add(br.readLine());
        }

        setN.retainAll(setM);
        Object[] array = setN.stream().sorted().toArray();
        System.out.println(array.length);
        for (Object o : array) {
            sb.append(o.toString()).append("\n");
        }
        System.out.println(sb);
    }
}