import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int n = arr[0];
        int m = arr[1];
        String[][] array = new String[n][m];
        for (int i = 0; i < n; i++) {
            array[i] = br.readLine().split("");
        }

        int min = 64;

        for (int i = 0; i <= n-8; i++) {
            for (int j = 0; j <= m-8; j++) {
                int count = 0;
                String temp = "W";
                for (int k = 0; k < 8; k++) {
                    for (int l = 0; l < 8; l++) {
                        if (!array[i + k][j + l].equals(temp)) {
                            count += 1;
                        }
                        temp = whatColor(temp);
                    }
                    temp = whatColor(temp);
                }
                if (min > count) {
                    min = count;
                }

                count = 0;
                temp = "B";
                for (int k = 0; k < 8; k++) {
                    for (int l = 0; l < 8; l++) {
                        if (!array[i + k][j + l].equals(temp)) {
                            count += 1;
                        }
                        temp = whatColor(temp);
                    }
                    temp = whatColor(temp);
                }
                if (min > count) {
                    min = count;
                }
            }
        }
        System.out.println(min);
    }

    public static String whatColor(String temp) {
        if (temp.equals("W")) {
            return "B";
        } else return "W";
    }
}