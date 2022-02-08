import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException  {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();

        int N = Integer.parseInt(input);
        int len = input.length();
        int result = 0;

        // 2자리 수 까지는 전부 등차수열이 가능 그래서 1~99까지는 전부 한수
        if (len <= 2) {
            result = N;
        } else {
            result += 99;
            int i;
            for (i = 100; i <= N; i++) {
                int hun = i / 100;
                int ten = (i % 100) / 10;
                int one = i % 10;

                if (hun - ten == ten - one) {
                    result += 1;
                }
            }
        }
        System.out.print(result);
        br.close();
    }
}