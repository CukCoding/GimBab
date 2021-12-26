import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
/*
    모든 순서쌍을 받은뒤 순서쌍의 첫번째 자리를 기준으로 오름차순 정렬한다.
 */

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //버퍼리더 객체 생성
        Scanner scan = new Scanner(System.in); //Scanner 객체 생성
        Queue<Integer> q = new LinkedList<>();

        int N = scan.nextInt();
        int[] arr = new int[N]; //컴퓨터 갯수만큼 배열 생성

        int i, cnt = 0;
        int T = scan.nextInt();
        int[][] com = new int[T][2]; //컴퓨터 갯수만큼 배열 생성

        for (i = 0 ; i < T ; i++) {
            String[] p = br.readLine().split(" ");
            com[i][0] = Integer.parseInt(p[0]);
            com[i][1] = Integer.parseInt(p[1]);
        }
        Arrays.sort(com, (num1, num2) -> {
            return Integer.compare(num1[0], num2[0]);
        });

        for (i = 0 ; i < T ; i++) {
            if (com[i][0] == 1) {
                q.add(com[i][1]);
            }
        }
        int target = 0;
        while (q.size() > 0) {
            target = q.poll();
            if (arr[target] == 1) {
                continue;
            }
            else {
                arr[target] = 1;
                cnt += 1;
                for (i = 0 ; i < T ; i++) {
                    if (com[i][0] == target) {
                        q.add(com[i][1]);
                    }
                }
            }
        }

        System.out.println(cnt);
        br.close();
    }
}