import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Segment {

    static long[] arr;
    static long[] segment;

    static long initSegment(int start, int end, int loc) {
        if(start == end) {
            segment[loc] = arr[start];
            return segment[loc];
        }
        int mid = (start + end) / 2;
        segment[loc] = initSegment(start, mid, loc*2) + initSegment(mid+1, end, loc*2+1);
        return segment[loc];
    }

    static long sum(int start, int end, int loc, int left, int right) {
        // 내가 구해야할 노드의 합이 범위 바깥에 있는지
        if (left > end || right < start) return 0;
            // 내가 구해야할 노드의 합이 범위 내부에 있는지
        else if(start >= left && end <= right) return segment[loc];
        int mid = (start + end) / 2;
        return sum(start, mid, loc*2, left, right) + sum(mid+1, end, loc*2+1, left, right);
    }

    static void update(int start, int end, int loc, long num, int idx) {
        if(idx < start || idx > end) return;
        segment[loc] += num;
        if(start == end) return;
        int mid = (start + end) / 2;
        update(start, mid, loc*2, num, idx);
        update(mid+1, end, loc*2+1, num, idx);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        // 배열 선언
        arr = new long[N];
        int h = (int)Math.ceil(Math.log(N) / Math.log(2));
        int size = (int)Math.pow(2, h+1);
        segment = new long[size+1];

        long[] rs = new long[K];
        int cnt = 0;

        for(int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        initSegment(0, N-1, 1);
        for(int i = 0; i < M+K; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            long c = Long.parseLong(st.nextToken());

            if(a == 1) {
                long gap = c - arr[b-1];
                arr[b-1] = c;
                update(0, N-1, 1, gap, b-1);
            } else {
                long result = sum(0, N-1, 1, b-1, (int)c-1);
                rs[cnt] = result;
                cnt++;
            }
        }
        for(int i = 0; i < K; i++) {
            System.out.print(rs[i]);
            if(i != K-1) System.out.println();
        }
    }
}