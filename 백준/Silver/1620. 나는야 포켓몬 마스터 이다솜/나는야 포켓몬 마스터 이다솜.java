import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int[] temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int n = temp[0];
        int m = temp[1];

        HashMap<Integer, String> pokemonList1 = new HashMap<>();
        HashMap<String, Integer> pokemonList2 = new HashMap<>();

        for (int i = 1; i < n+1; i++) {
            String input = br.readLine();
            pokemonList1.put(i, input);
            pokemonList2.put(input, i);
        }

        for (int i = 0; i < m; i++) {
            String input = br.readLine();
            try {
                int pokemonNumber = Integer.parseInt(input);
                sb.append(pokemonList1.get(pokemonNumber)).append("\n");
            } catch (NumberFormatException e) {
                sb.append(pokemonList2.get(input)).append("\n");
            }
        }
        System.out.println(sb);
    }
}