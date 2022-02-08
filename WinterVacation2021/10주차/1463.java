import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
/*
    N을 1로 만드는 최소 횟수는
    N-1을 1로 만드는 최소 횟수 + 1
    N/2를 1로 만드는 최소 횟수 + 1
    N/3을 1로 만드는 최소 횟수 + 1
 */

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int X = Integer.parseInt(br.readLine());
        //String[] s = br.readLine().split(" "); // 공백 구분해서 배열에 저장해준다

        int d[] = new int[X + 1];

        d[0] = 0; //0은 어짜피 나올 수 없기 때문에 0으로 초기화
        d[1] = 0; //1로 만들어야 되기 때문에 1이 시작점이라서 0부터 카운팅 시작
        for (int i = 2 ; i <= X ; i ++) {
            //2부터 1번 필요하기 i는 2부터 시작
            d[i] = d[i-1] + 1; //현재 숫자는 그전 숫자 +1 된 숫자이므로 무조건 전보다 +1번째로 만들어지는 숫자이다
            if (i % 2 == 0) {
                if (d[i] > d[i / 2] + 1) { // 현재 숫자의 카운팅 횟수가 2로 나눈 숫자 + 1 보다 크면 최소 카운트가 바뀐다
                    d[i] = d[i / 2] + 1;
                }
            }
            if (i % 3 == 0) {
                if (d[i] > d[i / 3] + 1) { // 현재 숫자의 카운팅 횟수가 3으로 나눈 숫자 + 1 보다 크면 최소 카운트가 바뀐다
                    d[i] = d[i / 3] + 1;
                }
            }
        }

        System.out.println(d[X]);
        br.close();
    }
}