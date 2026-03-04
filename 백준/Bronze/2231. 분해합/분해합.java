import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        int n = Integer.parseInt(input); //분해합

        int m = 0; //생성자

        for (int i = 0; i < n; i++) {
            int temp = i;
            String[] iArr = String.valueOf(i).split("");
            for (String s : iArr) {
                int parsedInt = Integer.parseInt(s);
                temp += parsedInt;

            }
            if (temp == n) {
                m = i;
                break;
            }
        }

        System.out.println(m);
    }
}