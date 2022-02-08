import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
/*
    계단의 최댓값을 각각 카피 배열에 넣어주는데 조건은 다음과 같다
    현재칸이 i 이면 최댓값은 copy[i-2] + stair[i] 또는
    copy[i-3] + stair[i-1] + stair[i] 의 값 둘중에 하나다

    2번째 조건에서 i-3칸의 최댓값에 더하는 이유는 해당칸의 전칸을 밟고 현재칸으로 올라온 경우
    3계단 연속을 밟는게 안되므로 전전칸을 밟을 수가 없기 때문에 계산할때 조건이 필요한 것이다.

    마지막 계단을 무조건 밟아야 하므로 조건에
    copy[i-2] + stair[i-1]은 존재 할 수가 없다.
 */

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        //String[] s = br.readLine().split(" "); // 공백 구분해서 배열에 저장해준다

        int[] stair = new int[N];
        int[] copy = new int[N]; //카피배열을 똑같은 크기로 만든다
        int i, num1 = 0, num2 = 0;

        for (i = 0 ; i < N ; i++) {
            stair[i] = Integer.parseInt(br.readLine());
        }

        if (N == 1) {
            copy[0] = stair[0];
        }
        else if (N == 2) {
            copy[1] = stair[0] + stair[1];
        }
        else if (N == 3) {
            copy[2] = Math.max(stair[0] + stair[2], stair[1] + stair[2]);
        }
        //첫번째 계단의 최댓값은 그대로고 두번째 계단의 최댓값은 첫번째 계단을 밟고 연속으로 두번째 계단을 밟앗을 경우이다.
        //3번째 계단의 최댓값은 1번째 계단 + 3번째 계단 이거나 2번째 계단 + 3번째 계단의 값이다.
        //계단이 3개 이하일 경우 조건을 따로줘서 최댓값을 구해야만 한다. 왜냐하면 기본 조건식에 현재 계단이 i번째일때
        // i-3의 값을 가져와야 하므로 i는 3부터 시작이어야 하기 때문이다.
        else if (N > 3) {
            copy[0] = stair[0];
            copy[1] = stair[0] + stair[1];
            copy[2] = Math.max(stair[0] + stair[2], stair[1] + stair[2]);
            for (i = 3 ; i < N; i++) {
                num1 = copy[i-3] + stair[i-1] + stair[i];
                num2 = copy[i-2] + stair[i];
                copy[i] = Math.max(num1, num2);
            }
        }

        System.out.println(copy[N-1]);
        br.close();
    }
}