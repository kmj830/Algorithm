import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

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
        ArrayList<String> result = new ArrayList<>(setN);
        result.sort(Comparator.naturalOrder());
        System.out.println(result.size());
        for (String s : result) {
            sb.append(s).append("\n");
        }
        System.out.println(sb);
    }
}