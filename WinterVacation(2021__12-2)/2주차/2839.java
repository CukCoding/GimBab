import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int cnt = 2000;
        int loop = N / 5;
        int total = N;
         for(int i = loop; i >= 0; i--) {
             int tmpCnt = i;
             if ((N - (5 * i)) % 3 == 0) {
                 int three = (N - (5 * i)) / 3;
                 tmpCnt += three;
                 if (tmpCnt < cnt) {
                     cnt = tmpCnt;
                 }
             }
         }
         if(cnt == 2000) {
             System.out.print(-1);
         } else {
             System.out.print(cnt);
         }
    }
}