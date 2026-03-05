import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static ArrayList<Integer> resultList = new ArrayList<>();
    public static boolean flag = true;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());


        addWeight(5, n, 1);
        addWeight(3, n, 1);
        if (resultList.isEmpty()) {
            System.out.println(-1);
        } else {
            System.out.println(Collections.min(resultList));
        }
    }
    public static void addWeight(int now, int target, int count) {
        if (now > target || !flag) {
            return;
        } else if (now == target) {
            resultList.add(count);
            flag = false;
        } else {
            addWeight(now + 5, target, count + 1);
            addWeight(now + 3, target, count + 1);
        }
    }
}