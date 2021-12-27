import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();

        int T = Integer.parseInt(input);

        int i = 0;
        ArrayList<ArrayList<Integer>> dp = new ArrayList<ArrayList<Integer>>();

        //피보나치 0은 무조건 1, 0
        ArrayList<Integer> fibozero = new ArrayList<Integer>();
        fibozero.add(1);
        fibozero.add(0);

        //피보나치 1은 무조건 0, 1
        ArrayList<Integer> fiboone = new ArrayList<Integer>();
        fiboone.add(0);
        fiboone.add(1);

        for (i = 0; i < T; i++) {
            dp.clear();
            dp.add(fibozero);
            dp.add(fiboone);
            int N = Integer.parseInt(br.readLine());

            if (N == 0) {
                System.out.println(dp.get(0).get(0) + " " + dp.get(0).get(1));
            } else if(N == 1) {
                System.out.println(dp.get(1).get(0) + " " + dp.get(1).get(1));
            } else {
                int j;
                for (j = 2; j <= N;j ++) {
                    ArrayList<Integer> fibo = new ArrayList<Integer>();
                    fibo.add(dp.get(j-1).get(0) + dp.get(j-2).get(0));
                    fibo.add(dp.get(j-1).get(1) + dp.get(j-2).get(1));
                    dp.add(fibo);
                }
                System.out.println(dp.get(N).get(0) + " " + dp.get(N).get(1));
            }

        }
        br.close();
    }
}