import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        int i = 0, L = 0, P = 0, V = 0, cnt = 0;
        while(true) {
            st = new StringTokenizer(br.readLine());
            L = Integer.parseInt(st.nextToken());
            P = Integer.parseInt(st.nextToken());
            V = Integer.parseInt(st.nextToken());

            if(L == 0 && P == 0 && V == 0) break;
            else {
                cnt++;
                int camping = V / P * L;
                int mod = V % P;
                if(mod > L) camping += L;
                else if(mod <= L) camping += mod;
                System.out.println("Case " + cnt + ": " + camping);
            }
        }
        br.close();
    }
}