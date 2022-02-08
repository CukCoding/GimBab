import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int K = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] pos = new int[N];
        for(int i = 0; i < N; i++) {
            pos[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(pos);

        int[] gap = new int[N-1];
        for(int i = 0; i < N-1; i++) {
            gap[i] = pos[i+1] - pos[i];
        }
        Arrays.sort(gap);

        int sum = 0;
        for (int i = N-2-(K-1); i >= 0; i--) {
            sum += gap[i];
        }
        System.out.print(sum);
    }
}