import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    // 보석 행렬
    public static int[][] acce;
    // 가방은 벡터 어레이로
    public static ArrayList<Integer> bag;
    // 최대 힙으로 쓸 녀석
    public static PriorityQueue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        acce = new int[N][2];
        bag = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            acce[i][0] = Integer.parseInt(st.nextToken());
            acce[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(acce, (o1, o2) -> {
            if(o1[0] == o2[0]) return Integer.compare(o1[1], o2[1]);
            else return Integer.compare(o1[0], o2[0]);
        });

        for (int i = 0; i < K; i++) {
            bag.add(Integer.parseInt(br.readLine()));
        }
        bag.sort(Comparator.naturalOrder());

        long result = 0;
        int idx = 0;

        for(int i = 0; i < K; i++) {
            int M = bag.get(i);
            while(idx < N && acce[idx][0] <= M) {
                queue.add(acce[idx][1]);
                idx++;
            }
            if (queue.size() != 0) {
                result = (long) result + queue.poll();
            }
        }
        System.out.print(result);
        br.close();
    }
}